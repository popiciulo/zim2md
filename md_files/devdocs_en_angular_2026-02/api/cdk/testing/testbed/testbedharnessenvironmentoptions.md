# TestbedHarnessEnvironmentOptions

TestbedHarnessEnvironmentOptions



# TestbedHarnessEnvironmentOptions

Options to configure the environment.

## API

```
interface TestbedHarnessEnvironmentOptions {
  queryFn: (selector: string, root: Element) => Iterable<Element> | ArrayLike<Element>;
}
```

### queryFn

`(selector: string, root: Element) => Iterable<Element> | ArrayLike<Element>`

The query function used to find DOM elements.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/cdk/testing/testbed/TestbedHarnessEnvironmentOptions>
