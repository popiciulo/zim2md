# input

input



# input

The [`input`](input) function allows declaration of Angular inputs in directives and components.

There are two variants of inputs that can be declared:

1. **Optional inputs** with an initial value.
2. **Required inputs** that consumers need to set.

By default, the [`input`](input) function will declare optional inputs that always have an initial value. Required inputs can be declared using the [`input.required()`](input#required) function.

Inputs are signals. The values of an input are exposed as a [`Signal`](signal). The signal always holds the latest value of the input that is bound from the parent.

## API

```
function input<T>();function input<T>(initialValue, opts?);function input<T>(initialValue, opts);function input<T, TransformT>(initialValue, opts);function input<T, TransformT>(initialValue, opts);function input.required<T>(opts?);function input.required<T, TransformT>(opts);
function input<T>(initialValue, opts?);
function input<T>(initialValue, opts);
function input<T, TransformT>(initialValue, opts);
function input<T, TransformT>(initialValue, opts);

function input.required<T>(opts?);
function input.required<T, TransformT>(opts);
```

```
function input<T>(): InputSignal<T | undefined>;
```

Initializes an input of type `T` with an initial value of `undefined`. Angular will implicitly use `undefined` as initial value.

@returns`InputSignal<T | undefined>`

```
function input<T>(initialValue: T, opts?: InputOptionsWithoutTransform<T> | undefined): InputSignal<T>;
```

Declares an input of type `T` with an explicit initial value.

@paraminitialValue`T`

@paramopts`InputOptionsWithoutTransform<T> | undefined`

@returns`InputSignal<T>`

```
function input<T>(initialValue: undefined, opts: InputOptionsWithoutTransform<T>): InputSignal<T | undefined>;
```

Declares an input of type `T|undefined` without an initial value, but with input options

@paraminitialValue`undefined`

@paramopts`InputOptionsWithoutTransform<T>`

@returns`InputSignal<T | undefined>`

```
function input<T, TransformT>(initialValue: T, opts: InputOptionsWithTransform<T, TransformT>): InputSignalWithTransform<T, TransformT>;
```

Declares an input of type `T` with an initial value and a transform function.

The input accepts values of type `TransformT` and the given transform function will transform the value to type `T`.

@paraminitialValue`T`

@paramopts`InputOptionsWithTransform<T, TransformT>`

@returns`InputSignalWithTransform<T, TransformT>`

```
function input<T, TransformT>(initialValue: undefined, opts: InputOptionsWithTransform<T | undefined, TransformT>): InputSignalWithTransform<T | undefined, TransformT>;
```

Declares an input of type `T|undefined` without an initial value and with a transform function.

The input accepts values of type `TransformT` and the given transform function will transform the value to type `T|undefined`.

@paraminitialValue`undefined`

@paramopts`InputOptionsWithTransform<T | undefined, TransformT>`

@returns`InputSignalWithTransform<T | undefined, TransformT>`

```
function input.required<T>(opts?: InputOptionsWithoutTransform<T> | undefined): InputSignal<T>;
```

Declares a required input of type `T`.

@paramopts`InputOptionsWithoutTransform<T> | undefined`

@returns`InputSignal<T>`

```
function input.required<T, TransformT>(opts: InputOptionsWithTransform<T, TransformT>): InputSignalWithTransform<T, TransformT>;
```

Declares a required input of type `T` with a transform function.

The input accepts values of type `TransformT` and the given transform function will transform the value to type `T`.

@paramopts`InputOptionsWithTransform<T, TransformT>`

@returns`InputSignalWithTransform<T, TransformT>`

## Usage Notes

To use signal-based inputs, import [`input`](input) from `@angular/core`.

```
import {input} from '@angular/core';
```

Inside your component, introduce a new class member and initialize it with a call to [`input`](input) or [`input.required`](input#required).

```
@Component({
  ...
})
export class UserProfileComponent {
  firstName = input<string>();             // Signal<string|undefined>
  lastName  = input.required<string>();    // Signal<string>
  age       = input(0)                     // Signal<number>
}
```

Inside your component template, you can display values of the inputs by calling the signal.

```
<span>{{firstName()}}</span>
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/input>
