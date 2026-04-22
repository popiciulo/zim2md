# output

output



# output

The [`output`](output) function allows declaration of Angular outputs in directives and components.

You can use outputs to emit values to parent directives and component. Parents can subscribe to changes via:

- template event bindings. For example, `(myOutput)="doSomething($event)"`
- programmatic subscription by using [`OutputRef#subscribe`](outputref#subscribe).

[Custom events with outputs](../../guide/components/outputs#customizing-output-names)

## API

```
function output<T = void>(opts?: OutputOptions | undefined): OutputEmitterRef<T>;
```

### output

`OutputEmitterRef<T>`

@paramopts`OutputOptions | undefined`

@returns`OutputEmitterRef<T>`

Usage notes

To use [`output()`](output), import the function from `@angular/core`.

```
import {output} from '@angular/core';
```

Inside your component, introduce a new class member and initialize it with a call to [`output`](output).

```
@Directive({
  ...
})
export class MyDir {
  nameChange = output<string>();    // OutputEmitterRef<string>
  onClick    = output();            // OutputEmitterRef<void>
}
```

You can emit values to consumers of your directive, by using the `emit` method from [`OutputEmitterRef`](outputemitterref).

```
updateName(newName: string): void {
  this.nameChange.emit(newName);
}
```

## Usage Notes

To use [`output()`](output), import the function from `@angular/core`.

```
import {output} from '@angular/core';
```

Inside your component, introduce a new class member and initialize it with a call to [`output`](output).

```
@Directive({
  ...
})
export class MyDir {
  nameChange = output<string>();    // OutputEmitterRef<string>
  onClick    = output();            // OutputEmitterRef<void>
}
```

You can emit values to consumers of your directive, by using the `emit` method from [`OutputEmitterRef`](outputemitterref).

```
updateName(newName: string): void {
  this.nameChange.emit(newName);
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/output>
