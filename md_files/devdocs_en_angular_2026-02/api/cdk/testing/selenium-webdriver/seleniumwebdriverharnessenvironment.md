# SeleniumWebDriverHarnessEnvironment

SeleniumWebDriverHarnessEnvironment



# SeleniumWebDriverHarnessEnvironment

A `HarnessEnvironment` implementation for WebDriver.

## API

```
class SeleniumWebDriverHarnessEnvironment extends HarnessEnvironment<
  () => webdriver.WebElement
> {
  protected constructor(rawRootElement: () => webdriver.WebElement, options?: WebDriverHarnessEnvironmentOptions | undefined): SeleniumWebDriverHarnessEnvironment;
  forceStabilize(): Promise<void>;
  protected getDocumentRoot(): () => webdriver.WebElement;
  protected createTestElement(element: () => webdriver.WebElement): TestElement;
  protected createEnvironment(element: () => webdriver.WebElement): HarnessEnvironment<() => webdriver.WebElement>;
  protected getAllRawElements(selector: string): Promise<(() => webdriver.WebElement)[]>;
  static getNativeElement(el: TestElement): webdriver.WebElement;
  static loader(driver: webdriver.WebDriver, options?: WebDriverHarnessEnvironmentOptions | undefined): HarnessLoader;
}
```

### constructor

`SeleniumWebDriverHarnessEnvironment`

@paramrawRootElement`() => webdriver.WebElement`

@paramoptions`WebDriverHarnessEnvironmentOptions | undefined`

@returns`SeleniumWebDriverHarnessEnvironment`

### forceStabilize

`Promise<void>`

Flushes change detection and async tasks captured in the Angular zone. In most cases it should not be necessary to call this manually. However, there may be some edge cases where it is needed to fully flush animation events.

@returns`Promise<void>`

### getDocumentRoot

`() => webdriver.WebElement`

Gets the root element for the document.

@returns`() => webdriver.WebElement`

### createTestElement

`TestElement`

Creates a `TestElement` from a raw element.

@paramelement`() => webdriver.WebElement`

@returns`TestElement`

### createEnvironment

`HarnessEnvironment<() => webdriver.WebElement>`

Creates a `HarnessLoader` rooted at the given raw element.

@paramelement`() => webdriver.WebElement`

@returns`HarnessEnvironment<() => webdriver.WebElement>`

### getAllRawElements

`Promise<(() => webdriver.WebElement)[]>`

Gets a list of all elements matching the given selector under this environment's root element.

@paramselector`string`

@returns`Promise<(() => webdriver.WebElement)[]>`

### getNativeElement

`webdriver.WebElement`

Gets the ElementFinder corresponding to the given TestElement.

@paramel`TestElement`

@returns`webdriver.WebElement`

### loader

`HarnessLoader`

Creates a `HarnessLoader` rooted at the document root.

@paramdriver`webdriver.WebDriver`

@paramoptions`WebDriverHarnessEnvironmentOptions | undefined`

@returns`HarnessLoader`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/cdk/testing/selenium-webdriver/SeleniumWebDriverHarnessEnvironment>
