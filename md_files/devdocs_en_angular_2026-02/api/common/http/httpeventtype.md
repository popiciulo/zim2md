# HttpEventType

HttpEventType



# HttpEventType

Type enumeration for the different kinds of [`HttpEvent`](httpevent).

[Receiving raw progress event](../../../guide/http/making-requests#receiving-raw-progress-events)

## API

```
enum HttpEventType {
  Sent: HttpEventType.Sent;
  UploadProgress: HttpEventType.UploadProgress;
  ResponseHeader: HttpEventType.ResponseHeader;
  DownloadProgress: HttpEventType.DownloadProgress;
  Response: HttpEventType.Response;
  User: HttpEventType.User;
}
```

### Sent

The request was sent out over the wire.

### UploadProgress

An upload progress event was received.

Note: The [`FetchBackend`](fetchbackend) doesn't support progress report on uploads.

### ResponseHeader

The response status code and headers were received.

### DownloadProgress

A download progress event was received.

### Response

The full response including the body was received.

### User

A custom event from an interceptor or a backend.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/HttpEventType>
