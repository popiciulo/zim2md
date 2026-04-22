# ComponentHarnessConstructor

ComponentHarnessConstructor



# ComponentHarnessConstructor

Constructor for a ComponentHarness subclass. To be a valid ComponentHarnessConstructor, the class must also have a static `hostSelector` property.

## API

```
interface ComponentHarnessConstructor<T extends ComponentHarness> {
  hostSelector: string;
}
```

### hostSelector

`string`

[`ComponentHarness`](componentharness) subclasses must specify a static `hostSelector` property that is used to find the host element for the corresponding component. This property should match the selector for the Angular component.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/cdk/testing/ComponentHarnessConstructor>
