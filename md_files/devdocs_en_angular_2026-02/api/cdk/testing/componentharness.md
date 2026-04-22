# ComponentHarness

ComponentHarness



# ComponentHarness

Base class for component test harnesses that all component harness authors should extend. This base component harness provides the basic ability to locate element and sub-component harnesses.

## API

```
abstract class ComponentHarness {
  constructor(locatorFactory: LocatorFactory): ComponentHarness;
  host(): Promise<TestElement>;
  protected documentRootLocatorFactory(): LocatorFactory;
  protected locatorFor<T extends (HarnessQuery<any> | string)[]>(...queries: T): () => Promise<LocatorFnResult<T>>;
  protected locatorForOptional<T extends (HarnessQuery<any> | string)[]>(...queries: T): () => Promise<LocatorFnResult<T> | null>;
  protected locatorForAll<T extends (HarnessQuery<any> | string)[]>(...queries: T): () => Promise<LocatorFnResult<T>[]>;
  protected forceStabilize(): Promise<void>;
  protected waitForTasksOutsideAngular(): Promise<void>;
}
```

### constructor

`ComponentHarness`

@paramlocatorFactory`LocatorFactory`

@returns`ComponentHarness`

### host

`Promise<TestElement>`

Gets a `Promise` for the [`TestElement`](testelement) representing the host element of the component.

@returns`Promise<TestElement>`

### documentRootLocatorFactory

`LocatorFactory`

Gets a [`LocatorFactory`](locatorfactory) for the document root element. This factory can be used to create locators for elements that a component creates outside of its own root element. (e.g. by appending to document.body).

@returns`LocatorFactory`

### locatorFor

`() => Promise<LocatorFnResult<T>>`

Creates an asynchronous locator function that can be used to find a [`ComponentHarness`](componentharness) instance or element under the host element of this [`ComponentHarness`](componentharness).

For example, given the following DOM and assuming `DivHarness.hostSelector` is `'div'`

```
<div id="d1"></div><div id="d2"></div>
```

then we expect:

```
await ch.locatorFor(DivHarness, 'div')() // Gets a `DivHarness` instance for #d1
await ch.locatorFor('div', DivHarness)() // Gets a `TestElement` instance for #d1
await ch.locatorFor('span')()            // Throws because the `Promise` rejects
```

@paramqueries`T`

A list of queries specifying which harnesses and elements to search for:

- A `string` searches for elements matching the CSS selector specified by the string.
- A [`ComponentHarness`](componentharness) constructor searches for [`ComponentHarness`](componentharness) instances matching the given class.
- A [`HarnessPredicate`](harnesspredicate) searches for [`ComponentHarness`](componentharness) instances matching the given predicate.

@returns`() => Promise<LocatorFnResult<T>>`

### locatorForOptional

`() => Promise<LocatorFnResult<T> | null>`

Creates an asynchronous locator function that can be used to find a [`ComponentHarness`](componentharness) instance or element under the host element of this [`ComponentHarness`](componentharness).

For example, given the following DOM and assuming `DivHarness.hostSelector` is `'div'`

```
<div id="d1"></div><div id="d2"></div>
```

then we expect:

```
await ch.locatorForOptional(DivHarness, 'div')() // Gets a `DivHarness` instance for #d1
await ch.locatorForOptional('div', DivHarness)() // Gets a `TestElement` instance for #d1
await ch.locatorForOptional('span')()            // Gets `null`
```

@paramqueries`T`

A list of queries specifying which harnesses and elements to search for:

- A `string` searches for elements matching the CSS selector specified by the string.
- A [`ComponentHarness`](componentharness) constructor searches for [`ComponentHarness`](componentharness) instances matching the given class.
- A [`HarnessPredicate`](harnesspredicate) searches for [`ComponentHarness`](componentharness) instances matching the given predicate.

@returns`() => Promise<LocatorFnResult<T> | null>`

### locatorForAll

`() => Promise<LocatorFnResult<T>[]>`

Creates an asynchronous locator function that can be used to find [`ComponentHarness`](componentharness) instances or elements under the host element of this [`ComponentHarness`](componentharness).

For example, given the following DOM and assuming `DivHarness.hostSelector` is `'div'` and `IdIsD1Harness.hostSelector` is `'#d1'`

```
<div id="d1"></div><div id="d2"></div>
```

then we expect:

```
// Gets [DivHarness for #d1, TestElement for #d1, DivHarness for #d2, TestElement for #d2]
await ch.locatorForAll(DivHarness, 'div')()
// Gets [TestElement for #d1, TestElement for #d2]
await ch.locatorForAll('div', '#d1')()
// Gets [DivHarness for #d1, IdIsD1Harness for #d1, DivHarness for #d2]
await ch.locatorForAll(DivHarness, IdIsD1Harness)()
// Gets []
await ch.locatorForAll('span')()
```

@paramqueries`T`

A list of queries specifying which harnesses and elements to search for:

- A `string` searches for elements matching the CSS selector specified by the string.
- A [`ComponentHarness`](componentharness) constructor searches for [`ComponentHarness`](componentharness) instances matching the given class.
- A [`HarnessPredicate`](harnesspredicate) searches for [`ComponentHarness`](componentharness) instances matching the given predicate.

@returns`() => Promise<LocatorFnResult<T>[]>`

### forceStabilize

`Promise<void>`

Flushes change detection and async tasks in the Angular zone. In most cases it should not be necessary to call this manually. However, there may be some edge cases where it is needed to fully flush animation events.

@returns`Promise<void>`

### waitForTasksOutsideAngular

`Promise<void>`

Waits for all scheduled or running async tasks to complete. This allows harness authors to wait for async tasks outside of the Angular zone.

@returns`Promise<void>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/cdk/testing/ComponentHarness>
