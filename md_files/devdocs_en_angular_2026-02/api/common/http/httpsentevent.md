# HttpSentEvent

HttpSentEvent



# HttpSentEvent

An event indicating that the request was sent to the server. Useful when a request may be retried multiple times, to distinguish between retries on the final event stream.

[Receiving raw progress events](../../../guide/http/making-requests#receiving-raw-progress-events)

## API

```
interface HttpSentEvent {
  type: HttpEventType.Sent;
}
```

### type

`HttpEventType.Sent`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/HttpSentEvent>
