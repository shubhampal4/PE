3.2 DAG Task Skipping – Debugging Explanation
Problem:

    A task is randomly skipped despite previous task success.

Possible Causes:

    trigger_rule mismatch (e.g., default is all_success)

    Upstream task was skipped (via branching/condition)

    Use of ShortCircuitOperator, BranchPythonOperator, etc.

How to Fix:

    Check Airflow UI for DAG flow and state

    Explicitly set:

task.trigger_rule = "all_done"

    Use TriggerRule.ALL_DONE when task should run even if upstream failed/skipped