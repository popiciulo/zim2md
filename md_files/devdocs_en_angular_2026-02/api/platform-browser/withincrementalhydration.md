# withIncrementalHydration

withIncrementalHydration



# withIncrementalHydration

Enables support for incremental hydration using the `hydrate` trigger syntax.

[provideClientHydration](provideclienthydration)

## API

```
function withIncrementalHydration(): HydrationFeature<HydrationFeatureKind.IncrementalHydration>;
```

### withIncrementalHydration

`HydrationFeature<HydrationFeatureKind.IncrementalHydration>`

Enables support for incremental hydration using the `hydrate` trigger syntax.

@returns`HydrationFeature<HydrationFeatureKind.IncrementalHydration>`

Usage notes

Basic example of how you can enable incremental hydration in your application when the [`bootstrapApplication`](bootstrapapplication) function is used:

```
bootstrapApplication(AppComponent, {
  providers: [provideClientHydration(withIncrementalHydration())]
});
```

## Usage Notes

Basic example of how you can enable incremental hydration in your application when the [`bootstrapApplication`](bootstrapapplication) function is used:

```
bootstrapApplication(AppComponent, {
  providers: [provideClientHydration(withIncrementalHydration())]
});
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/platform-browser/withIncrementalHydration>
