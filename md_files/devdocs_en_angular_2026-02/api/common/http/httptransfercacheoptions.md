# HttpTransferCacheOptions

HttpTransferCacheOptions



# HttpTransferCacheOptions

Options to configure how TransferCache should be used to cache requests made via HttpClient.

[Configuring the caching options](../../../guide/ssr#configuring-the-caching-options)

## API

```
type HttpTransferCacheOptions = {
  includeHeaders?: string[];
  filter?: (req: HttpRequest<unknown>) => boolean;
  includePostRequests?: boolean;
  includeRequestsWithAuthHeaders?: boolean;
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/HttpTransferCacheOptions>
