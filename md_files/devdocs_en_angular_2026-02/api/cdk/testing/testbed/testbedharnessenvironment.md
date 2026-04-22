# TestbedHarnessEnvironment

TestbedHarnessEnvironment



# TestbedHarnessEnvironment

A `HarnessEnvironment` implementation for Angular's Testbed.

## API

```
class TestbedHarnessEnvironment extends HarnessEnvironment<Element> {
  protected constructor(rawRootElement: Element, _fixture: ComponentFixture<unknown>, options?: TestbedHarnessEnvironmentOptions | undefined): TestbedHarnessEnvironment;
  forceStabilize(): Promise<void>;
  waitForTasksOutsideAngular(): Promise<void>;
  protected getDocumentRoot(): Element;
  protected createTestElement(element: Element): TestElement;
  protected createEnvironment(element: Element): HarnessEnvironment<Element>;
  protected getAllRawElements(selector: string): Promise<Element[]>;
  static loader(fixture: ComponentFixture<unknown>, options?: TestbedHarnessEnvironmentOptions | undefined): HarnessLoader;
  static documentRootLoader(fixture: ComponentFixture<unknown>, options?: TestbedHarnessEnvironmentOptions | undefined): HarnessLoader;
  static getNativeElement(el: TestElement): Element;
  static harnessForFixture<T extends ComponentHarness>(fixture: ComponentFixture<unknown>, harnessType: ComponentHarnessConstructor<T>, options?: TestbedHarnessEnvironmentOptions | undefined): Promise<T>;
}
```

### constructor

`TestbedHarnessEnvironment`

@paramrawRootElement`Element`

@param\_fixture`ComponentFixture<unknown>`

@paramoptions`TestbedHarnessEnvironmentOptions | undefined`

@returns`TestbedHarnessEnvironment`

### forceStabilize

`Promise<void>`

Flushes change detection and async tasks captured in the Angular zone. In most cases it should not be necessary to call this manually. However, there may be some edge cases where it is needed to fully flush animation events.

@returns`Promise<void>`

### waitForTasksOutsideAngular

`Promise<void>`

Waits for all scheduled or running async tasks to complete. This allows harness authors to wait for async tasks outside of the Angular zone.

@returns`Promise<void>`

### getDocumentRoot

`Element`

Gets the root element for the document.

@returns`Element`

### createTestElement

`TestElement`

Creates a `TestElement` from a raw element.

@paramelement`Element`

@returns`TestElement`

### createEnvironment

`HarnessEnvironment<Element>`

Creates a `HarnessLoader` rooted at the given raw element.

@paramelement`Element`

@returns`HarnessEnvironment<Element>`

### getAllRawElements

`Promise<Element[]>`

Gets a list of all elements matching the given selector under this environment's root element.

@paramselector`string`

@returns`Promise<Element[]>`

### loader

`HarnessLoader`

Creates a `HarnessLoader` rooted at the given fixture's root element.

@paramfixture`ComponentFixture<unknown>`

@paramoptions`TestbedHarnessEnvironmentOptions | undefined`

@returns`HarnessLoader`

### documentRootLoader

`HarnessLoader`

Creates a `HarnessLoader` at the document root. This can be used if harnesses are located outside of a fixture (e.g. overlays appended to the document body).

@paramfixture`ComponentFixture<unknown>`

@paramoptions`TestbedHarnessEnvironmentOptions | undefined`

@returns`HarnessLoader`

### getNativeElement

`Element`

Gets the native DOM element corresponding to the given TestElement.

@paramel`TestElement`

@returns`Element`

### harnessForFixture

`Promise<T>`

Creates an instance of the given harness type, using the fixture's root element as the harness's host element. This method should be used when creating a harness for the root element of a fixture, as components do not have the correct selector when they are created as the root of the fixture.

@paramfixture`ComponentFixture<unknown>`

@paramharnessType`ComponentHarnessConstructor<T>`

@paramoptions`TestbedHarnessEnvironmentOptions | undefined`

@returns`Promise<T>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/cdk/testing/testbed/TestbedHarnessEnvironment>
