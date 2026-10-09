# Optional Job State

Use a job folder only for long-running or iterative projects.
Suggested structure:

```
jobs/JOB_NAME/
  brief.md
  state.yaml
  master_prompt.md
  feedback.md
```

`state.yaml` can track:
- core_message
- exact_copy
- signature_mode
- reference_mode
- style
- aspect_ratio
- current_version
- unresolved_facts

Do not create heavy job state for simple one-off prompts.
