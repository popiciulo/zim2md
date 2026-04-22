# AsyncPipe

AsyncPipe



# AsyncPipe

Unwraps a value from an asynchronous primitive.

[Built-in Pipes](../../guide/templates/pipes#built-in-pipes)

## Pipe usage

```
{{ value_expression | async }}
```

## API

```
class AsyncPipe implements OnDestroy ,PipeTransform {
  constructor(ref: ChangeDetectorRef): AsyncPipe;
  transform<T>(obj: any): T | null;
  transform<T>(obj: null | undefined): null;
  transform<T>(obj: any): T | null;
}
```

### constructor

`AsyncPipe`

@paramref`ChangeDetectorRef`

@returns`AsyncPipe`

### ngOnDestroy

`void`

@returns`void`

### transform

3 overloads

@paramobj`any`

@returns`T | null`

@paramobj`null | undefined`

@returns`null`

@paramobj`any`

@returns`T | null`

## Description

Unwraps a value from an asynchronous primitive.

The `async` pipe subscribes to an `Observable` or `Promise` and returns the latest value it has emitted. When a new value is emitted, the `async` pipe marks the component to be checked for changes. When the component gets destroyed, the `async` pipe unsubscribes automatically to avoid potential memory leaks. When the reference of the expression changes, the `async` pipe automatically unsubscribes from the old `Observable` or `Promise` and subscribes to the new one.

---

## Exported by

- `CommonModule`

## Usage Notes

### Examples

This example binds a `Promise` to the view. Clicking the `Resolve` button resolves the promise.

```
@Component({
  selector: 'async-promise-pipe',
  imports: [AsyncPipe],
  template: `<div>
    <code>promise|async</code>:
    <button (click)="clicked()">{{ arrived ? 'Reset' : 'Resolve' }}</button>
    <span>Wait for it... {{ greeting | async }}</span>
  </div>`,
})
export class AsyncPromisePipeComponent {
  greeting: Promise<string> | null = null;
  arrived: boolean = false;

  private resolve: Function | null = null;

  constructor() {
    this.reset();
  }

  reset() {
    this.arrived = false;
    this.greeting = new Promise<string>((resolve, reject) => {
      this.resolve = resolve;
    });
  }

  clicked() {
    if (this.arrived) {
      this.reset();
    } else {
      this.resolve!('hi there!');
      this.arrived = true;
    }
  }
}
```

It's also possible to use `async` with Observables. The example below binds the `time` Observable to the view. The Observable continuously updates the view with the current time.

```
@Component({
  selector: 'async-observable-pipe',
  imports: [AsyncPipe],
  template: '<div><code>observable|async</code>: Time: {{ time | async }}</div>',
})
export class AsyncObservablePipeComponent {
  time = new Observable<string>((observer: Observer<string>) => {
    setInterval(() => observer.next(new Date().toString()), 1000);
  });
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/AsyncPipe>
