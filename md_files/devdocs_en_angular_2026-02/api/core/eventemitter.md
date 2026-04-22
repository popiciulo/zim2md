# EventEmitter

EventEmitter



# EventEmitter

Use in components with the [`@Output`](output) directive to emit custom events synchronously or asynchronously, and register handlers for those events by subscribing to an instance.

[Declaring outputs with the @Output decorator](../../guide/components/outputs#declaring-outputs-with-the-output-decorator)

## API

```
interface EventEmitter<T> extends Subject<T>, OutputRef<T> {
  emit(value?: T | undefined): void;
  subscribe(next?: ((value: T) => void) | undefined, error?: ((error: any) => void) | undefined, complete?: (() => void) | undefined): Subscription;
  subscribe(observerOrNext?: any, error?: any, complete?: any): Subscription;
}
```

### emit

`void`

Emits an event containing a given value.

@paramvalue`T | undefined`

The value to emit.

@returns`void`

### subscribe

`Subscription`

Registers handlers for events emitted by this instance.

@paramnext`((value: T) => void) | undefined`

When supplied, a custom handler for emitted events.

@paramerror`((error: any) => void) | undefined`

When supplied, a custom handler for an error notification from this emitter.

@paramcomplete`(() => void) | undefined`

When supplied, a custom handler for a completion notification from this emitter.

@returns`Subscription`

### subscribe

`Subscription`

Registers handlers for events emitted by this instance.

@paramobserverOrNext`any`

When supplied, a custom handler for emitted events, or an observer object.

@paramerror`any`

When supplied, a custom handler for an error notification from this emitter.

@paramcomplete`any`

When supplied, a custom handler for a completion notification from this emitter.

@returns`Subscription`

## Usage Notes

Extends [RxJS `Subject`](https://rxjs.dev/api/index/class/Subject) for Angular by adding the `emit()` method.

In the following example, a component defines two output properties that create event emitters. When the title is clicked, the emitter emits an open or close event to toggle the current visibility state.

```
@Component({
  selector: 'zippy',
  template: `
  <div class="zippy">
    <div (click)="toggle()">Toggle</div>
    <div [hidden]="!visible">
      <ng-content></ng-content>
    </div>
 </div>`})
export class Zippy {
  visible: boolean = true;
  @Output() open: EventEmitter<any> = new EventEmitter();
  @Output() close: EventEmitter<any> = new EventEmitter();

  toggle() {
    this.visible = !this.visible;
    if (this.visible) {
      this.open.emit(null);
    } else {
      this.close.emit(null);
    }
  }
}
```

Access the event object with the `$event` argument passed to the output event handler:

```
<zippy (open)="onOpen($event)" (close)="onClose($event)"></zippy>
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/EventEmitter>
