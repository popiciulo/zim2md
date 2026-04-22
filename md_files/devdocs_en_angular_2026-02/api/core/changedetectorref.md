# ChangeDetectorRef

ChangeDetectorRef



# ChangeDetectorRef

Base class that provides change detection functionality. A change-detection tree collects all views that are to be checked for changes. Use the methods to add and remove views from the tree, initiate change-detection, and explicitly mark views as *dirty*, meaning that they have changed and need to be re-rendered.

[Using change detection hooks](../../guide/components/lifecycle#using-change-detection-hooks)[Defining custom change detection](../../guide/components/lifecycle#defining-custom-change-detection)

## API

```
abstract class ChangeDetectorRef {
  abstract markForCheck(): void;
  abstract detach(): void;
  abstract detectChanges(): void;
  abstract checkNoChanges(): void;
  abstract reattach(): void;
}
```

### markForCheck

`void`

When a view uses the [`ChangeDetectionStrategy#OnPush`](changedetectionstrategy#OnPush) (checkOnce) change detection strategy, explicitly marks the view as changed so that it can be checked again.

Components are normally marked as dirty (in need of rerendering) when inputs have changed or events have fired in the view. Call this method to ensure that a component is checked even if these triggers have not occurred.

@returns`void`

### detach

`void`

Detaches this view from the change-detection tree. A detached view is not checked until it is reattached. Use in combination with `detectChanges()` to implement local change detection checks.

Detached views are not checked during change detection runs until they are re-attached, even if they are marked as dirty.

@returns`void`

### detectChanges

`void`

Checks this view and its children. Use in combination with [`ChangeDetectorRef#detach`](changedetectorref#detach) to implement local change detection checks.

@returns`void`

### checkNoChanges

`void`

Checks the change detector and its children, and throws if any changes are detected.

Use in development mode to verify that running change detection doesn't introduce other changes. Calling it in production mode is a noop.

@deprecated

This is a test-only API that does not have a place in production interface. `checkNoChanges` is already part of an [`ApplicationRef`](applicationref) tick when the app is running in dev mode. For more granular `checkNoChanges` validation, use `ComponentFixture`.

@returns`void`

### reattach

`void`

Re-attaches the previously detached view to the change detection tree. Views are attached to the tree by default.

@returns`void`

## Usage Notes

The following examples demonstrate how to modify default change-detection behavior to perform explicit detection when needed.

### Use markForCheck() with CheckOnce strategy

The following example sets the `OnPush` change-detection strategy for a component (`CheckOnce`, rather than the default `CheckAlways`), then forces a second check after an interval.

```
@Component({
  selector: 'app-root',
  template: `Number of ticks: {{ numberOfTicks }}`,
  changeDetection: ChangeDetectionStrategy.OnPush,
})
class AppComponent {
  numberOfTicks = 0;

  constructor(private ref: ChangeDetectorRef) {
    setInterval(() => {
      this.numberOfTicks++;
      // require view to be updated
      this.ref.markForCheck();
    }, 1000);
  }
}
```

### Detach change detector to limit how often check occurs

The following example defines a component with a large list of read-only data that is expected to change constantly, many times per second. To improve performance, we want to check and update the list less often than the changes actually occur. To do that, we detach the component's change detector and perform an explicit local check every five seconds.

```
class DataListProvider {
  // in a real application the returned data will be different every time
  get data() {
    return [1, 2, 3, 4, 5];
  }
}

@Component({
  selector: 'giant-list',
  template: `
  <ul>
    @for( d of dataProvider.data; track $index) {
      <li>Item {{ d }}</li>
    }
  </ul>`,
})
class GiantList {
  constructor(
    private ref: ChangeDetectorRef,
    public dataProvider: DataListProvider,
  ) {
    ref.detach();
    setInterval(() => {
      this.ref.detectChanges();
    }, 5000);
  }
}

@Component({
  selector: 'app',
  providers: [DataListProvider],
  imports: [GiantList],
  template: `<giant-list/>`,
})
class App {}
```

### Reattaching a detached component

The following example creates a component displaying live data. The component detaches its change detector from the main change detector tree when the `live` property is set to false, and reattaches it when the property becomes true.

```
class DataProvider {
  data = signal(1);
  constructor() {
    setInterval(() => {
      this.data.set(2);
    }, 500);
  }
}

@Component({
  selector: 'live-data',
  template: 'Data: {{dataProvider.data()}}',
})
class LiveData {
  live = input.required<boolean>();
  constructor(
    private ref: ChangeDetectorRef,
    public dataProvider: DataProvider,
  ) {
    effect(() => {
      if (this.live()) {
        this.ref.reattach();
      } else {
        this.ref.detach();
      }
    });
  }
}

@Component({
  selector: 'app',
  providers: [DataProvider],
  imports: [FormsModule, LiveData],
  template: `
    Live Update: <input type="checkbox" [(ngModel)]="live" />
    <live-data [live]="live"></live-data>
  `,
})
class App1 {
  live = true;
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/ChangeDetectorRef?tab=usage-notes>
