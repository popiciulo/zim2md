# enableProfiling

enableProfiling



# enableProfiling

Start listening to the Angular's internal performance-related events and route those to the Chrome DevTools performance panel. This enables Angular-specific data visualization when recording a performance profile directly in the Chrome DevTools.

[Profiling with the Chrome DevTools](https://angular.dev/best-practices/profiling-with-chrome-devtools#recording-a-profile)

## API

```
function enableProfiling(): () => void;
```

### enableProfiling

`() => void`

Start listening to the Angular's internal performance-related events and route those to the Chrome DevTools performance panel. This enables Angular-specific data visualization when recording a performance profile directly in the Chrome DevTools.

Note: integration is enabled in the development mode only, this operation is noop in the production mode.

@returns`() => void`

## Description

Start listening to the Angular's internal performance-related events and route those to the Chrome DevTools performance panel. This enables Angular-specific data visualization when recording a performance profile directly in the Chrome DevTools.

Note: integration is enabled in the development mode only, this operation is noop in the production mode.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/globals/enableProfiling>
