xmlTemplateServiceHealthRule_HEAP ="""
<health-rule>
        <name>%%RULENAME%%</name>
        <type>INFRASTRUCTURE</type>
        <description/>
        <enabled>true</enabled>
        <is-default>false</is-default>
        <always-enabled>true</always-enabled>
        <duration-min>5</duration-min>
        <wait-time-min>30</wait-time-min>
        <affected-entities-match-criteria>
            <affected-infra-match-criteria>
                <type>SPECIFIC_TIERS</type>
                <application-components>
                    <application-component>%%TIER%%</application-component>
                </application-components>
            </affected-infra-match-criteria>
        </affected-entities-match-criteria>
        <critical-execution-criteria>
            <entity-aggregation-scope>
                <type>ANY</type>
                <value>0</value>
            </entity-aggregation-scope>
            <policy-condition>
                <type>leaf</type>
                <display-name>heapUsage</display-name>
                <condition-value-type>ABSOLUTE</condition-value-type>
                <condition-value>90.0</condition-value>
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
                        <logical-metric-name>JVM|Memory:Heap|Used %</logical-metric-name>
                    </metric-definition>
                </metric-expression>
            </policy-condition>
        </critical-execution-criteria>
        <warning-execution-criteria>
            <entity-aggregation-scope>
                <type>ANY</type>
                <value>0</value>
            </entity-aggregation-scope>
            <policy-condition>
                <type>leaf</type>
                <display-name>heapUsage</display-name>
                <condition-value-type>ABSOLUTE</condition-value-type>
                <condition-value>80.0</condition-value>
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
                        <logical-metric-name>JVM|Memory:Heap|Used %</logical-metric-name>
                    </metric-definition>
                </metric-expression>
            </policy-condition>
        </warning-execution-criteria>
    </health-rule>
"""

xmlTemplateServiceHealthRule_GC = """
<health-rule>
        <name>%%RULENAME%%</name>
        <type>INFRASTRUCTURE</type>
        <description/>
        <enabled>true</enabled>
        <is-default>false</is-default>
        <always-enabled>true</always-enabled>
        <duration-min>5</duration-min>
        <wait-time-min>30</wait-time-min>
        <affected-entities-match-criteria>
            <affected-infra-match-criteria>
                <type>SPECIFIC_TIERS</type>
                <application-components>
                    <application-component>%%TIER%%</application-component>
                </application-components>
            </affected-infra-match-criteria>
        </affected-entities-match-criteria>
        <critical-execution-criteria>
            <entity-aggregation-scope>
                <type>ANY</type>
                <value>0</value>
            </entity-aggregation-scope>
            <policy-condition>
                <type>boolean</type>
                <operator>AND</operator>
                <condition1>
                    <type>leaf</type>
                    <display-name>gcMajorCollectionTimeSpent</display-name>
                    <condition-value-type>BASELINE_STANDARD_DEVIATION</condition-value-type>
                    <condition-value>2.0</condition-value>
                    <operator>GREATER_THAN</operator>
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
                            <logical-metric-name>JVM|Garbage Collection|Major Collection Time Spent Per Min (ms)</logical-metric-name>
                        </metric-definition>
                    </metric-expression>
                </condition1>
                <condition2>
                    <type>leaf</type>
                    <display-name>gcMajorCollectionTimeSpentTotal</display-name>
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
                            <logical-metric-name>JVM|Garbage Collection|Major Collection Time Spent Per Min (ms)</logical-metric-name>
                        </metric-definition>
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
                <operator>AND</operator>
                <condition1>
                    <type>leaf</type>
                    <display-name>gcMajorCollectionTimeSpent</display-name>
                    <condition-value-type>BASELINE_STANDARD_DEVIATION</condition-value-type>
                    <condition-value>1.0</condition-value>
                    <operator>GREATER_THAN</operator>
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
                            <logical-metric-name>JVM|Garbage Collection|Major Collection Time Spent Per Min (ms)</logical-metric-name>
                        </metric-definition>
                    </metric-expression>
                </condition1>
                <condition2>
                    <type>leaf</type>
                    <display-name>gcMajorCollectionTimeSpentTotal</display-name>
                    <condition-value-type>ABSOLUTE</condition-value-type>
                    <condition-value>2500.0</condition-value>
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
                            <logical-metric-name>JVM|Garbage Collection|Major Collection Time Spent Per Min (ms)</logical-metric-name>
                        </metric-definition>
                    </metric-expression>
                </condition2>
            </policy-condition>
        </warning-execution-criteria>
    </health-rule>
"""


xmlTemplateServiceHealthRule_THREADS = """
<health-rule>
        <name>%%RULENAME%%</name>
        <type>INFRASTRUCTURE</type>
        <description/>
        <enabled>true</enabled>
        <is-default>false</is-default>
        <always-enabled>true</always-enabled>
        <duration-min>5</duration-min>
        <wait-time-min>30</wait-time-min>
        <affected-entities-match-criteria>
            <affected-infra-match-criteria>
                <type>SPECIFIC_TIERS</type>
                <application-components>
                    <application-component>%%TIER%%</application-component>
                </application-components>
            </affected-infra-match-criteria>
        </affected-entities-match-criteria>
        <critical-execution-criteria>
            <entity-aggregation-scope>
                <type>ANY</type>
                <value>0</value>
            </entity-aggregation-scope>
            <policy-condition>
                <type>boolean</type>
                <operator>AND</operator>
                <condition1>
                    <type>leaf</type>
                    <display-name>threadUsage</display-name>
                    <condition-value-type>BASELINE_PERCENTAGE</condition-value-type>
                    <condition-value>50.0</condition-value>
                    <operator>GREATER_THAN</operator>
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
                            <logical-metric-name>JVM|Threads|Current No. of Threads</logical-metric-name>
                        </metric-definition>
                    </metric-expression>
                </condition1>
                <condition2>
                    <type>leaf</type>
                    <display-name>threadUsage</display-name>
                    <condition-value-type>BASELINE_PERCENTAGE</condition-value-type>
                    <condition-value>90.0</condition-value>
                    <operator>LESS_THAN</operator>
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
                            <logical-metric-name>JVM|Threads|Current No. of Threads</logical-metric-name>
                        </metric-definition>
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
                <operator>AND</operator>
                <condition1>
                    <type>leaf</type>
                    <display-name>threadUsage</display-name>
                    <condition-value-type>BASELINE_PERCENTAGE</condition-value-type>
                    <condition-value>25.0</condition-value>
                    <operator>GREATER_THAN</operator>
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
                            <logical-metric-name>JVM|Threads|Current No. of Threads</logical-metric-name>
                        </metric-definition>
                    </metric-expression>
                </condition1>
                <condition2>
                    <type>leaf</type>
                    <display-name>threadUsage</display-name>
                    <condition-value-type>BASELINE_PERCENTAGE</condition-value-type>
                    <condition-value>50.0</condition-value>
                    <operator>LESS_THAN</operator>
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
                            <logical-metric-name>JVM|Threads|Current No. of Threads</logical-metric-name>
                        </metric-definition>
                    </metric-expression>
                </condition2>
            </policy-condition>
        </warning-execution-criteria>
    </health-rule>
"""

xmlTemplateServiceHealthRule_JDBC = """
<health-rule>
        <name>%%RULENAME%%</name>
        <type>JMX</type>
        <description>Application Infrastructure Performance|%%TIER%%|JMX|JDBC Connection Pools</description>
        <enabled>true</enabled>
        <is-default>false</is-default>
        <always-enabled>true</always-enabled>
        <duration-min>5</duration-min>
        <wait-time-min>30</wait-time-min>
        <affected-entities-match-criteria>
            <affected-jmx-match-criteria>
                <type>JMX_INSTANCE_NAME</type>
                <metric-path-prefix>JMX|JDBC Connection Pools</metric-path-prefix>
                <node-match-criteria>
                    <type>NODES_OF_SPECIFC_TIERS</type>
                    <node-types>
                        <node-type>APP_AGENT</node-type>
                    </node-types>
                    <node-meta-info-match-criteria/>
                    <vm-sys-properties/>
                    <env-properties/>
                </node-match-criteria>
                <components>
                    <application-component>%%TIER%%</application-component>
                </components>
                <jmx-match-criteria>
                    <type>ANY</type>
                    <jmx-instance-names/>
                </jmx-match-criteria>
            </affected-jmx-match-criteria>
        </affected-entities-match-criteria>
        <critical-execution-criteria>
            <entity-aggregation-scope>
                <type>ANY</type>
                <value>0</value>
            </entity-aggregation-scope>
            <policy-condition>
                <type>leaf</type>
                <display-name>usedConnections</display-name>
                <condition-value-type>ABSOLUTE</condition-value-type>
                <condition-value>90.0</condition-value>
                <operator>GREATER_THAN</operator>
                <condition-expression>{activeConnections} / ({maxConnections} / 100)</condition-expression>
                <use-active-baseline>false</use-active-baseline>
                <trigger-on-no-data>false</trigger-on-no-data>
                <metric-expression>
                    <type>boolean</type>
                    <operator>DIVIDE</operator>
                    <expression1>
                        <type>leaf</type>
                        <function-type>VALUE</function-type>
                        <value>0</value>
                        <is-literal-expression>false</is-literal-expression>
                        <display-name>activeConnections</display-name>
                        <metric-definition>
                            <type>LOGICAL_METRIC</type>
                            <logical-metric-name>Active Connections</logical-metric-name>
                        </metric-definition>
                    </expression1>
                    <expression2>
                        <type>boolean</type>
                        <operator>DIVIDE</operator>
                        <expression1>
                            <type>leaf</type>
                            <function-type>VALUE</function-type>
                            <value>0</value>
                            <is-literal-expression>false</is-literal-expression>
                            <display-name>maxConnections</display-name>
                            <metric-definition>
                                <type>LOGICAL_METRIC</type>
                                <logical-metric-name>Maximum Connections</logical-metric-name>
                            </metric-definition>
                        </expression1>
                        <expression2>
                            <type>leaf</type>
                            <value>100</value>
                            <is-literal-expression>true</is-literal-expression>
                        </expression2>
                    </expression2>
                </metric-expression>
            </policy-condition>
        </critical-execution-criteria>
        <warning-execution-criteria>
            <entity-aggregation-scope>
                <type>ANY</type>
                <value>0</value>
            </entity-aggregation-scope>
            <policy-condition>
                <type>leaf</type>
                <display-name>usedConnections</display-name>
                <condition-value-type>ABSOLUTE</condition-value-type>
                <condition-value>80.0</condition-value>
                <operator>GREATER_THAN</operator>
                <condition-expression>{activeConnections} / ({maxConnections} / 100)</condition-expression>
                <use-active-baseline>false</use-active-baseline>
                <trigger-on-no-data>false</trigger-on-no-data>
                <metric-expression>
                    <type>boolean</type>
                    <operator>DIVIDE</operator>
                    <expression1>
                        <type>leaf</type>
                        <function-type>VALUE</function-type>
                        <value>0</value>
                        <is-literal-expression>false</is-literal-expression>
                        <display-name>activeConnections</display-name>
                        <metric-definition>
                            <type>LOGICAL_METRIC</type>
                            <logical-metric-name>Active Connections</logical-metric-name>
                        </metric-definition>
                    </expression1>
                    <expression2>
                        <type>boolean</type>
                        <operator>DIVIDE</operator>
                        <expression1>
                            <type>leaf</type>
                            <function-type>VALUE</function-type>
                            <value>0</value>
                            <is-literal-expression>false</is-literal-expression>
                            <display-name>maxConnections</display-name>
                            <metric-definition>
                                <type>LOGICAL_METRIC</type>
                                <logical-metric-name>Maximum Connections</logical-metric-name>
                            </metric-definition>
                        </expression1>
                        <expression2>
                            <type>leaf</type>
                            <value>100</value>
                            <is-literal-expression>true</is-literal-expression>
                        </expression2>
                    </expression2>
                </metric-expression>
            </policy-condition>
        </warning-execution-criteria>
    </health-rule>
"""
