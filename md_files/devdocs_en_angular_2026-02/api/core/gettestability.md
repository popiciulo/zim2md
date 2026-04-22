# GetTestability

GetTestability



# GetTestability

Adapter interface for retrieving the [`Testability`](testability) service associated for a particular context.

## API

```
interface GetTestability {
  addToWindow(registry: TestabilityRegistry): void;
  findTestabilityInTree(registry: TestabilityRegistry, elem: any, findInAncestors: boolean): Testability | null;
}
```

### addToWindow

`void`

@paramregistry`TestabilityRegistry`

@returns`void`

### findTestabilityInTree

`Testability | null`

@paramregistry`TestabilityRegistry`

@paramelem`any`

@paramfindInAncestors`boolean`

@returns`Testability | null`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/GetTestability>
