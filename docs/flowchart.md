# Toolchange Flowchart

This flowchart assumes a `fsensor_delay` of 2000ms.

``` mermaid
graph TD
  A[T1] --> B[Toolchange T=1];
  B[Toolchange T=1] --> C{Same tool?};
  C --> |No| D{Previous filament loaded?};
  C --> |Yes| E{Do nothing};
  D --> |Yes| F[MMMS_UNLOAD];
  F --> G[DESYNC_TOOL TOOL=0];
  G --> H[G4 P2000];
  H --> I[CHECK_FSENSOR V=0];
  D --> |No| J[SYNC_TOOL TOOL=1];
  I --> J;
  J --> K[MMMS_LOAD];
  K --> L[G4 P2000];
  L --> M[CHECK_FSENSOR V=1];
  M --> N[Save new previous extruder]
```