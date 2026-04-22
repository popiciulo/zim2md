# BootstrapOptions

BootstrapOptions



# BootstrapOptions

Provides additional options to the bootstrapping process.

Deprecation warning

Configure [`NgZone`](ngzone) in the `providers` array of the application module instead.

## API

```
interface BootstrapOptions {
  ngZone?: NgZone | "zone.js" | "noop" | undefined;
  ngZoneEventCoalescing?: boolean | undefined;
  ngZoneRunCoalescing?: boolean | undefined;
}
```

### ngZone

`NgZone | "zone.js" | "noop" | undefined`

@deprecated

BootstrapOptions is deprecated. Provide [`NgZone`](ngzone) in the `providers` array of the module instead.

Optionally specify which [`NgZone`](ngzone) should be used when not configured in the providers.

- Provide your own [`NgZone`](ngzone) instance.
- `zone.js` - Use default [`NgZone`](ngzone) which requires `Zone.js`.
- `noop` - Use `NoopNgZone` which does nothing.

### ngZoneEventCoalescing

`boolean | undefined`

@deprecated

BootstrapOptions is deprecated. Use [`provideZoneChangeDetection`](providezonechangedetection) instead to configure coalescing.

Optionally specify coalescing event change detections or not. Consider the following case.

```
<div (click)="doSomething()">
  <button (click)="doSomethingElse()"></button>
</div>
```

When button is clicked, because of the event bubbling, both event handlers will be called and 2 change detections will be triggered. We can coalesce such kind of events to only trigger change detection only once.

By default, this option will be false. So the events will not be coalesced and the change detection will be triggered multiple times. And if this option be set to true, the change detection will be triggered async by scheduling a animation frame. So in the case above, the change detection will only be triggered once.

### ngZoneRunCoalescing

`boolean | undefined`

@deprecated

BootstrapOptions is deprecated. Use [`provideZoneChangeDetection`](providezonechangedetection) instead to configure coalescing.

Optionally specify if [`NgZone#run()`](ngzone#run) method invocations should be coalesced into a single change detection.

Consider the following case.

```
for (let i = 0; i < 10; i ++) {
  ngZone.run(() => {
    // do something
  });
}
```

This case triggers the change detection multiple times. With ngZoneRunCoalescing options, all change detections in an event loop trigger only once. In addition, the change detection executes in requestAnimation.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/BootstrapOptions>
