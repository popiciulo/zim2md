# HttpProgressEvent

HttpProgressEvent



# HttpProgressEvent

Base interface for progress events.

[Receiving raw progress events](../../../guide/http/making-requests#receiving-raw-progress-events)

## API

```
interface HttpProgressEvent {
  type: HttpEventType.UploadProgress | HttpEventType.DownloadProgress;
  loaded: number;
  total?: number | undefined;
}
```

### type

`HttpEventType.UploadProgress | HttpEventType.DownloadProgress`

Progress event type is either upload or download.

### loaded

`number`

Number of bytes uploaded or downloaded.

### total

`number | undefined`

Total number of bytes to upload or download. Depending on the request or response, this may not be computable and thus may not be present.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/HttpProgressEvent>
