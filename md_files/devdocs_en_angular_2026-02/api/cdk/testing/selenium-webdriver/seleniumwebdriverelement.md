# SeleniumWebDriverElement

SeleniumWebDriverElement



# SeleniumWebDriverElement

A `TestElement` implementation for WebDriver.

## API

```
class SeleniumWebDriverElement implements TestElement {
  constructor(element: () => webdriver.WebElement, _stabilize: () => Promise<void>): SeleniumWebDriverElement;
  blur(): Promise<void>;
  clear(): Promise<void>;
  click(modifiers?: any): Promise<void>;
  click(location: "center", modifiers?: any): Promise<void>;
  click(relativeX: number, relativeY: number, modifiers?: any): Promise<void>;
  rightClick(relativeX: number, relativeY: number, modifiers?: any): Promise<void>;
  focus(): Promise<void>;
  getCssValue(property: string): Promise<string>;
  hover(): Promise<void>;
  mouseAway(): Promise<void>;
  sendKeys(...keys: any[]): Promise<void>;
  sendKeys(modifiers: ModifierKeys, ...keys: any[]): Promise<void>;
  text(options?: any): Promise<string>;
  setContenteditableValue(value: string): Promise<void>;
  getAttribute(name: string): Promise<string | null>;
  hasClass(name: string): Promise<boolean>;
  getDimensions(): Promise<ElementDimensions>;
  getProperty<T = any>(name: string): Promise<T>;
  setInputValue(newValue: string): Promise<void>;
  selectOptions(...optionIndexes: number[]): Promise<void>;
  matchesSelector(selector: string): Promise<boolean>;
  isFocused(): Promise<boolean>;
  dispatchEvent(name: string, data?: Record<string, EventData> | undefined): Promise<void>;
}
```

### constructor

`SeleniumWebDriverElement`

@paramelement`() => webdriver.WebElement`

@param\_stabilize`() => Promise<void>`

@returns`SeleniumWebDriverElement`

### blur

`Promise<void>`

Blur the element.

@returns`Promise<void>`

### clear

`Promise<void>`

Clear the element's input (for input and textarea elements only).

@returns`Promise<void>`

### click

3 overloads

Click the element at the default location for the current environment. If you need to guarantee the element is clicked at a specific location, consider using `click('center')` or `click(x, y)` instead.

@parammodifiers`any`

@returns`Promise<void>`

Click the element at the element's center.

@paramlocation`"center"`

@parammodifiers`any`

@returns`Promise<void>`

Click the element at the specified coordinates relative to the top-left of the element.

@paramrelativeX`number`

Coordinate within the element, along the X-axis at which to click.

@paramrelativeY`number`

Coordinate within the element, along the Y-axis at which to click.

@parammodifiers`any`

Modifier keys held while clicking

@returns`Promise<void>`

### rightClick

`Promise<void>`

Right clicks on the element at the specified coordinates relative to the top-left of it.

@paramrelativeX`number`

Coordinate within the element, along the X-axis at which to click.

@paramrelativeY`number`

Coordinate within the element, along the Y-axis at which to click.

@parammodifiers`any`

Modifier keys held while clicking

@returns`Promise<void>`

### focus

`Promise<void>`

Focus the element.

@returns`Promise<void>`

### getCssValue

`Promise<string>`

Get the computed value of the given CSS property for the element.

@paramproperty`string`

@returns`Promise<string>`

### hover

`Promise<void>`

Hovers the mouse over the element.

@returns`Promise<void>`

### mouseAway

`Promise<void>`

Moves the mouse away from the element.

@returns`Promise<void>`

### sendKeys

2 overloads

Sends the given string to the input as a series of key presses. Also fires input events and attempts to add the string to the Element's value.

@paramkeys`any[]`

@returns`Promise<void>`

Sends the given string to the input as a series of key presses. Also fires input events and attempts to add the string to the Element's value.

@parammodifiers`ModifierKeys`

@paramkeys`any[]`

@returns`Promise<void>`

### text

`Promise<string>`

Gets the text from the element.

@paramoptions`any`

Options that affect what text is included.

@returns`Promise<string>`

### setContenteditableValue

`Promise<void>`

Sets the value of a `contenteditable` element.

@paramvalue`string`

Value to be set on the element.

@returns`Promise<void>`

### getAttribute

`Promise<string | null>`

Gets the value for the given attribute from the element.

@paramname`string`

@returns`Promise<string | null>`

### hasClass

`Promise<boolean>`

Checks whether the element has the given class.

@paramname`string`

@returns`Promise<boolean>`

### getDimensions

`Promise<ElementDimensions>`

Gets the dimensions of the element.

@returns`Promise<ElementDimensions>`

### getProperty

`Promise<T>`

Gets the value of a property of an element.

@paramname`string`

@returns`Promise<T>`

### setInputValue

`Promise<void>`

Sets the value of a property of an input.

@paramnewValue`string`

@returns`Promise<void>`

### selectOptions

`Promise<void>`

Selects the options at the specified indexes inside of a native `select` element.

@paramoptionIndexes`number[]`

@returns`Promise<void>`

### matchesSelector

`Promise<boolean>`

Checks whether this element matches the given selector.

@paramselector`string`

@returns`Promise<boolean>`

### isFocused

`Promise<boolean>`

Checks whether the element is focused.

@returns`Promise<boolean>`

### dispatchEvent

`Promise<void>`

Dispatches an event with a particular name.

@paramname`string`

Name of the event to be dispatched.

@paramdata`Record<string, EventData> | undefined`

@returns`Promise<void>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/cdk/testing/selenium-webdriver/SeleniumWebDriverElement>
