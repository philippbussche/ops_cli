from commands.templates import widgets
from util import CommandInvocationError, CommandExecutionError
import copy
import json
import requests


# Create a text widget
def create_text_widget(height, width, x, y, name):
    textwidget = copy.deepcopy(widgets.text_widget)
    textwidget["text"] = str(name)
    textwidget["x"] = x
    textwidget["y"] = y
    textwidget["height"] = height
    textwidget["width"] = width
    return textwidget


# Create a status widget
def create_status_widget(height, width, x, y, hrname):
    statuswidget = copy.deepcopy(widgets.status_light_widget)
    statuswidget["height"] = height
    statuswidget["width"] = width
    statuswidget["x"] = x
    statuswidget["y"] = y
    statuswidget["healthRule"]["entityName"] = hrname
    return statuswidget


# Create a label widget
def create_label_widget(height, width, x, y, label):
    labelwidget = copy.deepcopy(widgets.status_dashboard_label_widget)
    labelwidget["height"] = height
    labelwidget["width"] = width
    labelwidget["x"] = x
    labelwidget["y"] = y
    labelwidget["text"] = "<center>" + label + "</center>"
    return labelwidget


# Create a questionmark widget
def create_questionmark_widget(height, width, x, y):
    questionmarkwidget = copy.deepcopy(widgets.questionmark_widget)
    questionmarkwidget["height"] = height
    questionmarkwidget["width"] = width
    questionmarkwidget["x"] = x
    questionmarkwidget["y"] = y
    return questionmarkwidget


# Create an overlay widget
def create_overlay_widget(height, width, x, y):
    overlaywidget = copy.deepcopy(widgets.overlay_widget)
    overlaywidget["height"] = height
    overlaywidget["width"] = width
    overlaywidget["x"] = x
    overlaywidget["y"] = y
    return overlaywidget


# Create a headline widget
def create_headline_widget(y, headline):
    headlinewidget = copy.deepcopy(widgets.status_dashboard_headline_widget)
    headlinewidget["y"] = y
    headlinewidget["text"] = '<u>%s</u>' % (headline)
    return headlinewidget


# Create a status dashboard
def create_status_dashboard(name):
    statusdashboard = copy.deepcopy(widgets.status_dashboard)
    statusdashboard['name'] = name
    return statusdashboard


# Create a eventstream widget
def create_eventstream_widget(application_name, tier):
    eventstreamwidget = copy.deepcopy(widgets.eventstream_widget)
    eventstreamwidget["eventFilterTemplate"]["applicationName"] = application_name
    eventstreamwidget["eventFilterTemplate"]["specificEntityNamesByType"]["APPLICATION_COMPONENT"][0]["applicationName"] = application_name
    eventstreamwidget["eventFilterTemplate"]["specificEntityNamesByType"]["APPLICATION_COMPONENT"][0]["entityName"] = tier
    return eventstreamwidget


# Create a link widget to be placed under the eventstream widget
def create_eventstream_link_widget(drilldown_url):
    widget = copy.deepcopy(widgets.eventstream_link_widget)
    widget['drillDownUrl'] = drilldown_url
    return widget


# Create a row in the status dashboard
def create_row_in_status_dashboard(status_widget_height,
                                    status_widget_width,
                                    x, y,
                                    application,
                                    headline,
                                    rules,
                                    bts=None,
                                    drilldown_url=None):
    row = []
    widgets = []
    headline_widget = create_headline_widget(y, headline)
    row.append(headline_widget)
    y = y + 50
    for key in rules:
        status_widget = create_status_widget(
                            status_widget_height,
                            status_widget_width,
                            x, y,
                            key
                        )
        status_widget["healthRule"]["applicationName"] = application
        overlay_widget = create_overlay_widget(
                            status_widget_height,
                            status_widget_width,
                            x, y + 2
                        )
        label = rules[key]['displayName'].upper()
        label_widget = create_label_widget(
                            30,
                            status_widget_width,
                            x, y + 2 + (status_widget_height/3),
                            label
                        )
        if bts is not None:
            # This seems to be a row showing BT status lights
            # Let's make sure we set a proper drilldown
            for k, v in bts.iteritems():
                if v['btName'] == rules[key]['btName']:
                    url = drilldown_url + '&businessTransaction=%s' % (k)
                    label_widget['drillDownUrl'] = url
        questionmark_widget = create_questionmark_widget(
                            status_widget_height / 5,
                            status_widget_width / 5,
                            x + 55, y + 2 + (status_widget_height / 2))
        row.append(status_widget)
        row.append(overlay_widget)
        row.append(label_widget)
        row.append(questionmark_widget)
        x = x + status_widget_width + 100
    return row


# Create dashboard json file
def create_dashboard_file(filename, dashboard):
    dashboard_file = open(filename, 'w')
    dashboard_file.truncate()
    dashboard_file.write(json.dumps(dashboard, indent=4))
    dashboard_file.close()
    return filename

# Post dashboard json file to Controller in order to import new Dashboard
def post_dashboard_file(filename, **kwargs):
    files = {'file': (filename, open(filename, 'rb'), 'application/json')}
    endpoint = 'http://%s/controller/CustomDashboardImportExportServlet' \
        % (kwargs['controllerHost'])
    try:
        r = requests.post(endpoint,
                          auth=(kwargs['username'], kwargs['password']),
                          files=files)
        return r._content
    except Exception as e:
        raise CommandInvocationError('Error posting dashboard JSON.')
