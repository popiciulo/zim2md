# BaseHarnessFilters

BaseHarnessFilters



# BaseHarnessFilters

A set of criteria that can be used to filter a list of [`ComponentHarness`](componentharness) instances.

## API

```
interface BaseHarnessFilters {
  selector?: string | undefined;
  ancestor?: string | undefined;
}
```

### selector

`string | undefined`

Only find instances whose host element matches the given selector.

### ancestor

`string | undefined`

Only find instances that are nested under an element with the given selector.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/cdk/testing/BaseHarnessFilters>
