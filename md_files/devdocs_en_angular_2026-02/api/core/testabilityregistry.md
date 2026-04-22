# TestabilityRegistry

TestabilityRegistry



# TestabilityRegistry

A global registry of [`Testability`](testability) instances for specific elements.

## API

```
class TestabilityRegistry {
  registerApplication(token: any, testability: Testability): void;
  unregisterApplication(token: any): void;
  unregisterAllApplications(): void;
  getTestability(elem: any): Testability | null;
  getAllTestabilities(): Testability[];
  getAllRootElements(): any[];
  findTestabilityInTree(elem: Node, findInAncestors?: boolean): Testability | null;
}
```

### registerApplication

`void`

Registers an application with a testability hook so that it can be tracked

@paramtoken`any`

token of application, root element

@paramtestability`Testability`

Testability hook

@returns`void`

### unregisterApplication

`void`

Unregisters an application.

@paramtoken`any`

token of application, root element

@returns`void`

### unregisterAllApplications

`void`

Unregisters all applications

@returns`void`

### getTestability

`Testability | null`

Get a testability hook associated with the application

@paramelem`any`

root element

@returns`Testability | null`

### getAllTestabilities

`Testability[]`

Get all registered testabilities

@returns`Testability[]`

### getAllRootElements

`any[]`

Get all registered applications(root elements)

@returns`any[]`

### findTestabilityInTree

`Testability | null`

Find testability of a node in the Tree

@paramelem`Node`

node

@paramfindInAncestors`boolean`

whether finding testability in ancestors if testability was not found in current node

@returns`Testability | null`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/TestabilityRegistry>
