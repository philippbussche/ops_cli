xmlTemplateTransactionHealthRule_BT = """
    <health-rule>
        <name>%%RULENAME%%</name>
        <type>BUSINESS_TRANSACTION</type>
        <description/>
        <enabled>true</enabled>
        <is-default>false</is-default>
        <always-enabled>true</always-enabled>
        <duration-min>5</duration-min>
        <wait-time-min>30</wait-time-min>
        <affected-entities-match-criteria>
            <affected-bt-match-criteria>
                <type>SPECIFIC</type>
                <business-transactions>
                    <business-transaction application-component="%%TIER%%">%%BTNAME%%</business-transaction>
                </business-transactions>
            </affected-bt-match-criteria>
        </affected-entities-match-criteria>
        <critical-execution-criteria>
            <entity-aggregation-scope>
                <type>ANY</type>
                <value>0</value>
            </entity-aggregation-scope>
            <policy-condition>
                <type>boolean</type>
                <operator>OR</operator>
                <condition1>
                    <type>leaf</type>
                    <display-name>responseTime</display-name>
                    <condition-value-type>ABSOLUTE</condition-value-type>
                    <condition-value>5000.0</condition-value>
                    <operator>GREATER_THAN</operator>
                    <condition-expression/>
                    <use-active-baseline>false</use-active-baseline>
                    <trigger-on-no-data>false</trigger-on-no-data>
                    <metric-expression>
                        <type>leaf</type>
                        <function-type>VALUE</function-type>
                        <value>0</value>
                        <is-literal-expression>false</is-literal-expression>
                        <display-name>null</display-name>
                        <metric-definition>
                            <type>LOGICAL_METRIC</type>
                            <logical-metric-name>Average Response Time (ms)</logical-metric-name>
                        </metric-definition>
                    </metric-expression>
                </condition1>
                <condition2>
                    <type>leaf</type>
                    <display-name>errorRateInPercent</display-name>
                    <condition-value-type>ABSOLUTE</condition-value-type>
                    <condition-value>10.0</condition-value>
                    <operator>GREATER_THAN</operator>
                    <condition-expression>{Errors}*100/{Calls}</condition-expression>
                    <use-active-baseline>false</use-active-baseline>
                    <trigger-on-no-data>false</trigger-on-no-data>
                    <metric-expression>
                        <type>boolean</type>
                        <operator>DIVIDE</operator>
                        <expression1>
                            <type>boolean</type>
                            <operator>MULTIPLY</operator>
                            <expression1>
                                <type>leaf</type>
                                <function-type>SUM</function-type>
                                <value>0</value>
                                <is-literal-expression>false</is-literal-expression>
                                <display-name>Errors</display-name>
                                <metric-definition>
                                    <type>LOGICAL_METRIC</type>
                                    <logical-metric-name>Errors per Minute</logical-metric-name>
                                </metric-definition>
                            </expression1>
                            <expression2>
                                <type>leaf</type>
                                <value>100</value>
                                <is-literal-expression>true</is-literal-expression>
                            </expression2>
                        </expression1>
                        <expression2>
                            <type>leaf</type>
                            <function-type>SUM</function-type>
                            <value>0</value>
                            <is-literal-expression>false</is-literal-expression>
                            <display-name>Calls</display-name>
                            <metric-definition>
                                <type>LOGICAL_METRIC</type>
                                <logical-metric-name>Calls per Minute</logical-metric-name>
                            </metric-definition>
                        </expression2>
                    </metric-expression>
                </condition2>
            </policy-condition>
        </critical-execution-criteria>
        <warning-execution-criteria>
            <entity-aggregation-scope>
                <type>ANY</type>
                <value>0</value>
            </entity-aggregation-scope>
            <policy-condition>
                <type>boolean</type>
                <operator>OR</operator>
                <condition1>
                    <type>leaf</type>
                    <display-name>responseTime</display-name>
                    <condition-value-type>BASELINE_STANDARD_DEVIATION</condition-value-type>
                    <condition-value>3.0</condition-value>
                    <operator>NOT_EQUALS</operator>
                    <condition-expression/>
                    <use-active-baseline>true</use-active-baseline>
                    <trigger-on-no-data>false</trigger-on-no-data>
                    <metric-expression>
                        <type>leaf</type>
                        <function-type>VALUE</function-type>
                        <value>0</value>
                        <is-literal-expression>false</is-literal-expression>
                        <display-name>null</display-name>
                        <metric-definition>
                            <type>LOGICAL_METRIC</type>
                            <logical-metric-name>Average Response Time (ms)</logical-metric-name>
                        </metric-definition>
                    </metric-expression>
                </condition1>
                <condition2>
                    <type>leaf</type>
                    <display-name>errorRateInPercent</display-name>
                    <condition-value-type>ABSOLUTE</condition-value-type>
                    <condition-value>5.0</condition-value>
                    <operator>GREATER_THAN</operator>
                    <condition-expression>{Errors}*100/{Calls}</condition-expression>
                    <use-active-baseline>false</use-active-baseline>
                    <trigger-on-no-data>false</trigger-on-no-data>
                    <metric-expression>
                        <type>boolean</type>
                        <operator>DIVIDE</operator>
                        <expression1>
                            <type>boolean</type>
                            <operator>MULTIPLY</operator>
                            <expression1>
                                <type>leaf</type>
                                <function-type>SUM</function-type>
                                <value>0</value>
                                <is-literal-expression>false</is-literal-expression>
                                <display-name>Errors</display-name>
                                <metric-definition>
                                    <type>LOGICAL_METRIC</type>
                                    <logical-metric-name>Errors per Minute</logical-metric-name>
                                </metric-definition>
                            </expression1>
                            <expression2>
                                <type>leaf</type>
                                <value>100</value>
                                <is-literal-expression>true</is-literal-expression>
                            </expression2>
                        </expression1>
                        <expression2>
                            <type>leaf</type>
                            <function-type>SUM</function-type>
                            <value>0</value>
                            <is-literal-expression>false</is-literal-expression>
                            <display-name>Calls</display-name>
                            <metric-definition>
                                <type>LOGICAL_METRIC</type>
                                <logical-metric-name>Calls per Minute</logical-metric-name>
                            </metric-definition>
                        </expression2>
                    </metric-expression>
                </condition2>
            </policy-condition>
        </warning-execution-criteria>
    </health-rule>
"""
