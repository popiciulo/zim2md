# manualChangeDetection

manualChangeDetection



# manualChangeDetection

Disables the harness system's auto change detection for the duration of the given function.

## API

```
function manualChangeDetection<T>(fn: () => Promise<T>): Promise<T>;
```

### manualChangeDetection

`Promise<T>`

Disables the harness system's auto change detection for the duration of the given function.

@paramfn`() => Promise<T>`

The function to disable auto change detection for.

@returns`Promise<T>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/cdk/testing/manualChangeDetection>
