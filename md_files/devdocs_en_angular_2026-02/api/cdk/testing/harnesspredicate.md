# HarnessPredicate

HarnessPredicate



# HarnessPredicate

A class used to associate a ComponentHarness class with predicate functions that can be used to filter instances of the class to be matched.

## API

```
class HarnessPredicate<T extends ComponentHarness> {
  constructor(harnessType: ComponentHarnessConstructor<T>, options: BaseHarnessFilters): HarnessPredicate<T>;
  override harnessType: ComponentHarnessConstructor<T>;
  add(description: string, predicate: AsyncPredicate<T>): this;
  addOption<O>(name: string, option: O | undefined, predicate: AsyncOptionPredicate<T, O>): this;
  filter(harnesses: T[]): Promise<T[]>;
  evaluate(harness: T): Promise<boolean>;
  getDescription(): string;
  getSelector(): string;
  static stringMatches(value: string | Promise<string | null> | null, pattern: string | RegExp | null): Promise<boolean>;
}
```

### constructor

`HarnessPredicate<T>`

@paramharnessType`ComponentHarnessConstructor<T>`

@paramoptions`BaseHarnessFilters`

@returns`HarnessPredicate<T>`

### harnessType

`ComponentHarnessConstructor<T>`

### add

`this`

Adds a predicate function to be run against candidate harnesses.

@paramdescription`string`

A description of this predicate that may be used in error messages.

@parampredicate`AsyncPredicate<T>`

An async predicate function.

@returns`this`

### addOption

`this`

Adds a predicate function that depends on an option value to be run against candidate harnesses. If the option value is undefined, the predicate will be ignored.

@paramname`string`

The name of the option (may be used in error messages).

@paramoption`O | undefined`

The option value.

@parampredicate`AsyncOptionPredicate<T, O>`

The predicate function to run if the option value is not undefined.

@returns`this`

### filter

`Promise<T[]>`

Filters a list of harnesses on this predicate.

@paramharnesses`T[]`

The list of harnesses to filter.

@returns`Promise<T[]>`

### evaluate

`Promise<boolean>`

Evaluates whether the given harness satisfies this predicate.

@paramharness`T`

The harness to check

@returns`Promise<boolean>`

### getDescription

`string`

Gets a description of this predicate for use in error messages.

@returns`string`

### getSelector

`string`

Gets the selector used to find candidate elements.

@returns`string`

### stringMatches

`Promise<boolean>`

Checks if the specified nullable string value matches the given pattern.

@paramvalue`string | Promise<string | null> | null`

The nullable string value to check, or a Promise resolving to the nullable string value.

@parampattern`string | RegExp | null`

The pattern the value is expected to match. If `pattern` is a string, `value` is expected to match exactly. If `pattern` is a regex, a partial match is allowed. If `pattern` is `null`, the value is expected to be `null`.

@returns`Promise<boolean>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/cdk/testing/HarnessPredicate>
