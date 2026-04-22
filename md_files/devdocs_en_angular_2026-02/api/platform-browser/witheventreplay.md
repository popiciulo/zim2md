# withEventReplay

withEventReplay



# withEventReplay

Enables support for replaying user events (e.g. `click`s) that happened on a page before hydration logic has completed. Once an application is hydrated, all captured events are replayed and relevant event listeners are executed.

[provideClientHydration](provideclienthydration)

## API

```
function withEventReplay(): HydrationFeature<HydrationFeatureKind.EventReplay>;
```

### withEventReplay

`HydrationFeature<HydrationFeatureKind.EventReplay>`

Enables support for replaying user events (e.g. `click`s) that happened on a page before hydration logic has completed. Once an application is hydrated, all captured events are replayed and relevant event listeners are executed.

@returns`HydrationFeature<HydrationFeatureKind.EventReplay>`

Usage notes

Basic example of how you can enable event replay in your application when [`bootstrapApplication`](bootstrapapplication) function is used:

```
bootstrapApplication(AppComponent, {
  providers: [provideClientHydration(withEventReplay())]
});
```

## Usage Notes

Basic example of how you can enable event replay in your application when [`bootstrapApplication`](bootstrapapplication) function is used:

```
bootstrapApplication(AppComponent, {
  providers: [provideClientHydration(withEventReplay())]
});
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/platform-browser/withEventReplay>
