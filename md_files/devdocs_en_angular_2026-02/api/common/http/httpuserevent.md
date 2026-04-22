# HttpUserEvent

HttpUserEvent



# HttpUserEvent

A user-defined event.

[Receiving raw progress events](../../../guide/http/making-requests#receiving-raw-progress-events)

## API

```
interface HttpUserEvent<T> {
  type: HttpEventType.User;
}
```

### type

`HttpEventType.User`

## Description

A user-defined event.

Grouping all custom events under this type ensures they will be handled and forwarded by all implementations of interceptors.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/HttpUserEvent>
