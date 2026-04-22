# AutoChangeDetectionStatus

AutoChangeDetectionStatus



# AutoChangeDetectionStatus

The status of the test harness auto change detection. If not diabled test harnesses will automatically trigger change detection after every action (such as a click) and before every read (such as getting the text of an element).

## API

```
interface AutoChangeDetectionStatus {
  isDisabled: boolean;
  onDetectChangesNow?: (() => void) | undefined;
}
```

### isDisabled

`boolean`

Whether auto change detection is disabled.

### onDetectChangesNow

`(() => void) | undefined`

An optional callback, if present it indicates that change detection should be run immediately, while handling the status change. The callback should then be called as soon as change detection is done.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/cdk/testing/AutoChangeDetectionStatus>
