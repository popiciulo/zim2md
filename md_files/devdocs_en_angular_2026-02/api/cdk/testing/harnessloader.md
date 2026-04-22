# HarnessLoader

HarnessLoader



# HarnessLoader

Interface used to load ComponentHarness objects. This interface is used by test authors to instantiate [`ComponentHarness`](componentharness)es.

## API

```
interface HarnessLoader {
  getChildLoader(selector: string): Promise<HarnessLoader>;
  getAllChildLoaders(selector: string): Promise<HarnessLoader[]>;
  getHarness<T extends ComponentHarness>(query: HarnessQuery<T>): Promise<T>;
  getHarnessOrNull<T extends ComponentHarness>(query: HarnessQuery<T>): Promise<T | null>;
  getHarnessAtIndex<T extends ComponentHarness>(query: HarnessQuery<T>, index: number): Promise<T>;
  getAllHarnesses<T extends ComponentHarness>(query: HarnessQuery<T>): Promise<T[]>;
  countHarnesses<T extends ComponentHarness>(query: HarnessQuery<T>): Promise<number>;
  hasHarness<T extends ComponentHarness>(query: HarnessQuery<T>): Promise<boolean>;
}
```

### getChildLoader

`Promise<HarnessLoader>`

Searches for an element with the given selector under the current instances's root element, and returns a [`HarnessLoader`](harnessloader) rooted at the matching element. If multiple elements match the selector, the first is used. If no elements match, an error is thrown.

@paramselector`string`

The selector for the root element of the new [`HarnessLoader`](harnessloader)

@returns`Promise<HarnessLoader>`

### getAllChildLoaders

`Promise<HarnessLoader[]>`

Searches for all elements with the given selector under the current instances's root element, and returns an array of [`HarnessLoader`](harnessloader)s, one for each matching element, rooted at that element.

@paramselector`string`

The selector for the root element of the new [`HarnessLoader`](harnessloader)

@returns`Promise<HarnessLoader[]>`

### getHarness

`Promise<T>`

Searches for an instance of the component corresponding to the given harness type under the [`HarnessLoader`](harnessloader)'s root element, and returns a [`ComponentHarness`](componentharness) for that instance. If multiple matching components are found, a harness for the first one is returned. If no matching component is found, an error is thrown.

@paramquery`HarnessQuery<T>`

A query for a harness to create

@returns`Promise<T>`

### getHarnessOrNull

`Promise<T | null>`

Searches for an instance of the component corresponding to the given harness type under the [`HarnessLoader`](harnessloader)'s root element, and returns a [`ComponentHarness`](componentharness) for that instance. If multiple matching components are found, a harness for the first one is returned. If no matching component is found, null is returned.

@paramquery`HarnessQuery<T>`

A query for a harness to create

@returns`Promise<T | null>`

### getHarnessAtIndex

`Promise<T>`

Searches for an instance of the component corresponding to the given harness type under the [`HarnessLoader`](harnessloader)'s root element, and returns a [`ComponentHarness`](componentharness) for the instance on the page at the given index. If no matching component exists at that index, an error is thrown.

@paramquery`HarnessQuery<T>`

A query for a harness to create

@paramindex`number`

The zero-indexed offset of the matching component instance to return

@returns`Promise<T>`

### getAllHarnesses

`Promise<T[]>`

Searches for all instances of the component corresponding to the given harness type under the [`HarnessLoader`](harnessloader)'s root element, and returns a list [`ComponentHarness`](componentharness) for each instance.

@paramquery`HarnessQuery<T>`

A query for a harness to create

@returns`Promise<T[]>`

### countHarnesses

`Promise<number>`

Searches for all instances of the component corresponding to the given harness type under the [`HarnessLoader`](harnessloader)'s root element, and returns the total count of all matching components.

@paramquery`HarnessQuery<T>`

A query for a harness to create

@returns`Promise<number>`

### hasHarness

`Promise<boolean>`

Searches for an instance of the component corresponding to the given harness type under the [`HarnessLoader`](harnessloader)'s root element, and returns a boolean indicating if any were found.

@paramquery`HarnessQuery<T>`

A query for a harness to create

@returns`Promise<boolean>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/cdk/testing/HarnessLoader>
