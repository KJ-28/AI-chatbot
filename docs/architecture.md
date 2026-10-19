## Architecture
```
                KK AI Framework

                       │
                 Chat Pipeline
                       │
        ┌──────────────┴──────────────┐
        ▼                             ▼
 Prompt Engine                  Memory Engine
        │
        ▼
 Prompt Builder
        │
        ▼
 Prompt Stages
```

---



## AI Security Pipeline架构图
```
             User
              │
              ▼
        Input Filter
              │
              ▼
    Prompt Injection
              │
              ▼
      Secret Masking
              │
              ▼
       Risk Engine
              │
              ▼
        Audit Logger
              │
              ▼
             LLM


```