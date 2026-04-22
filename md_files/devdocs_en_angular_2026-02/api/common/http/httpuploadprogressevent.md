# HttpUploadProgressEvent

HttpUploadProgressEvent



# HttpUploadProgressEvent

An upload progress event.

[Receiving raw progress events](../../../guide/http/making-requests#receiving-raw-progress-events)

## API

```
interface HttpUploadProgressEvent extends HttpProgressEvent {
  type: HttpEventType.UploadProgress;
  override loaded: number;
  override total?: number | undefined;
}
```

### type

`HttpEventType.UploadProgress`

### loaded

`number`

Number of bytes uploaded or downloaded.

### total

`number | undefined`

Total number of bytes to upload or download. Depending on the request or response, this may not be computable and thus may not be present.

## Description

An upload progress event.

Note: The [`FetchBackend`](fetchbackend) doesn't support progress report on uploads.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/HttpUploadProgressEvent>
