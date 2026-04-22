# ComponentFixture

ComponentFixture



# ComponentFixture

Fixture for debugging and testing a component.

## API

```
class ComponentFixture<T> {
  debugElement: DebugElement;
  componentInstance: T;
  nativeElement: any;
  elementRef: ElementRef<any>;
  changeDetectorRef: ChangeDetectorRef;
  ngZone: NgZone | null;
  override componentRef: ComponentRef<T>;
  detectChanges(checkNoChanges?: boolean): void;
  checkNoChanges(): void;
  autoDetectChanges(autoDetect: boolean): void;
  autoDetectChanges(): void;
  isStable(): boolean;
  whenStable(): Promise<any>;
  getDeferBlocks(): Promise<DeferBlockFixture[]>;
  whenRenderingDone(): Promise<any>;
  destroy(): void;
}
```

### debugElement

`DebugElement`

The DebugElement associated with the root element of this component.

### componentInstance

`T`

The instance of the root component class.

### nativeElement

`any`

The native element at the root of the component.

### elementRef

`ElementRef<any>`

The ElementRef for the element at the root of the component.

### changeDetectorRef

`ChangeDetectorRef`

The ChangeDetectorRef for the component

### ngZone

`NgZone | null`

### componentRef

`ComponentRef<T>`

### detectChanges

`void`

Trigger a change detection cycle for the component.

@paramcheckNoChanges`boolean`

@returns`void`

### checkNoChanges

`void`

Do a change detection run to make sure there were no changes.

@returns`void`

### autoDetectChanges

2 overloads

Set whether the fixture should autodetect changes.

Also runs detectChanges once so that any existing change is detected.

@deprecated

For `autoDetect: true`, use `autoDetectChanges()`. We have not seen a use-case for `autoDetect: false` but `changeDetectorRef.detach()` is a close equivalent.

@paramautoDetect`boolean`

Whether to autodetect changes. By default, `true`.

@returns`void`

Enables automatically synchronizing the view, as it would in an application.

Also runs detectChanges once so that any existing change is detected.

@returns`void`

### isStable

`boolean`

Return whether the fixture is currently stable or has async tasks that have not been completed yet.

@returns`boolean`

### whenStable

`Promise<any>`

Get a promise that resolves when the fixture is stable.

This can be used to resume testing after events have triggered asynchronous activity or asynchronous change detection.

@returns`Promise<any>`

### getDeferBlocks

`Promise<DeferBlockFixture[]>`

Retrieves all defer block fixtures in the component fixture.

@returns`Promise<DeferBlockFixture[]>`

### whenRenderingDone

`Promise<any>`

Get a promise that resolves when the ui state is stable following animations.

@returns`Promise<any>`

### destroy

`void`

Trigger component destruction.

@returns`void`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/testing/ComponentFixture>
