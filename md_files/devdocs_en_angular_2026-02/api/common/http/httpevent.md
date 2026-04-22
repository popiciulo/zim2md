# HttpEvent

HttpEvent



# HttpEvent

Union type for all possible events on the response stream.

[Intercepting response events](../../../guide/http/interceptors#intercepting-response-events)

## API

```
type HttpEvent<T> = | HttpSentEvent
  | HttpHeaderResponse
  | HttpResponse<T>
  | HttpDownloadProgressEvent
  | HttpUploadProgressEvent
  | HttpUserEvent<T>
```

## Description

Union type for all possible events on the response stream.

Typed according to the expected type of the response.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/HttpEvent>
