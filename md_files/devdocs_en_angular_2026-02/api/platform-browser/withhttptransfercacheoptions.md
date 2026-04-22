# withHttpTransferCacheOptions

withHttpTransferCacheOptions



# withHttpTransferCacheOptions

The function accepts an object, which allows to configure cache parameters, such as which headers should be included (no headers are included by default), whether POST requests should be cached or a callback function to determine if a particular request should be cached.

[Configuring HTTP transfer cache options](../../guide/ssr#caching-data-when-using-httpclient)

## API

```
function withHttpTransferCacheOptions(
  options: HttpTransferCacheOptions,
): HydrationFeature<HydrationFeatureKind.HttpTransferCacheOptions>;
```

### withHttpTransferCacheOptions

`HydrationFeature<HydrationFeatureKind.HttpTransferCacheOptions>`

The function accepts an object, which allows to configure cache parameters, such as which headers should be included (no headers are included by default), whether POST requests should be cached or a callback function to determine if a particular request should be cached.

@paramoptions`HttpTransferCacheOptions`

@returns`HydrationFeature<HydrationFeatureKind.HttpTransferCacheOptions>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/platform-browser/withHttpTransferCacheOptions>
