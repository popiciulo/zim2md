# HarnessQuery

HarnessQuery



# HarnessQuery

A query for a [`ComponentHarness`](componentharness), which is expressed as either a [`ComponentHarnessConstructor`](componentharnessconstructor) or a [`HarnessPredicate`](harnesspredicate).

## API

```
type HarnessQuery<T extends ComponentHarness> = | ComponentHarnessConstructor<T>
  | HarnessPredicate<T>
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/cdk/testing/HarnessQuery>
