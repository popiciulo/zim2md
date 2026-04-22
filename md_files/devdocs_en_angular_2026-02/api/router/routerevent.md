# RouterEvent

RouterEvent



# RouterEvent

Base for events the router goes through, as opposed to events tied to a specific route. Fired one time for any given navigation.

[Event](event)[Router events summary](../../guide/routing/router-reference#router-events)

## API

```
class RouterEvent {
  constructor(id: number, url: string): RouterEvent;
  override id: number;
  override url: string;
}
```

### constructor

`RouterEvent`

@paramid`number`

A unique ID that the router assigns to every router navigation.

@paramurl`string`

The URL that is the destination for this navigation.

@returns`RouterEvent`

### id

`number`

A unique ID that the router assigns to every router navigation.

### url

`string`

The URL that is the destination for this navigation.

## Description

Base for events the router goes through, as opposed to events tied to a specific route. Fired one time for any given navigation.

The following code shows how a class subscribes to router events.

```
import {Event, RouterEvent, Router} from '@angular/router';

class MyService {
  constructor(public router: Router) {
    router.events.pipe(
       filter((e: Event | RouterEvent): e is RouterEvent => e instanceof RouterEvent)
    ).subscribe((e: RouterEvent) => {
      // Do something
    });
  }
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/RouterEvent>
