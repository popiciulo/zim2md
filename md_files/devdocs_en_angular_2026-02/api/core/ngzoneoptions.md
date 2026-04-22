# NgZoneOptions

NgZoneOptions



# NgZoneOptions

Used to configure event and run coalescing with [`provideZoneChangeDetection`](providezonechangedetection).

[provideZoneChangeDetection](providezonechangedetection)

## API

```
interface NgZoneOptions {
  eventCoalescing?: boolean | undefined;
  runCoalescing?: boolean | undefined;
}
```

### eventCoalescing

`boolean | undefined`

Optionally specify coalescing event change detections or not. Consider the following case.

```
<div (click)="doSomething()">
  <button (click)="doSomethingElse()"></button>
</div>
```

When button is clicked, because of the event bubbling, both event handlers will be called and 2 change detections will be triggered. We can coalesce such kind of events to trigger change detection only once.

By default, this option is set to false, meaning events will not be coalesced, and change detection will be triggered multiple times. If this option is set to true, change detection will be triggered once in the scenario described above.

### runCoalescing

`boolean | undefined`

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
<https://angular.dev/api/core/NgZoneOptions>
