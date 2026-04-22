# HttpDownloadProgressEvent

HttpDownloadProgressEvent



# HttpDownloadProgressEvent

A download progress event.

[Receiving raw progress events](../../../guide/http/making-requests#receiving-raw-progress-events)

## API

```
interface HttpDownloadProgressEvent extends HttpProgressEvent {
  type: HttpEventType.DownloadProgress;
  partialText?: string | undefined;
  override loaded: number;
  override total?: number | undefined;
}
```

### type

`HttpEventType.DownloadProgress`

### partialText

`string | undefined`

The partial response body as downloaded so far.

Only present if the responseType was `text`.

### loaded

`number`

Number of bytes uploaded or downloaded.

### total

`number | undefined`

Total number of bytes to upload or download. Depending on the request or response, this may not be computable and thus may not be present.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/HttpDownloadProgressEvent>
