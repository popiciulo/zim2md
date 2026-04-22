# SwPush

SwPush



# SwPush

Subscribe and listen to [Web Push Notifications](https://developer.mozilla.org/en-US/docs/Web/API/Push_API/Best_Practices) through Angular Service Worker.

[Push Notifications](https://developers.google.com/web/fundamentals/codelabs/push-notifications/)[Angular Push Notifications](https://blog.angular-university.io/angular-push-notifications/)[MDN: Push API](https://developer.mozilla.org/en-US/docs/Web/API/Push_API)[MDN: Notifications API](https://developer.mozilla.org/en-US/docs/Web/API/Notifications_API)[MDN: Web Push API Notifications best practices](https://developer.mozilla.org/en-US/docs/Web/API/Push_API/Best_Practices)[Push notifications guide](https://angular.dev/ecosystem/service-workers/push-notifications)

## API

```
class SwPush {
  constructor(sw: NgswCommChannel): SwPush;
  readonly messages: Observable<object>;
  readonly notificationClicks: Observable<{ action: string; notification: NotificationOptions & { title: string; }; }>;
  readonly notificationCloses: Observable<{ action: string; notification: NotificationOptions & { title: string; }; }>;
  readonly pushSubscriptionChanges: Observable<{ oldSubscription: PushSubscription | null; newSubscription: PushSubscription | null; }>;
  readonly subscription: Observable<PushSubscription | null>;
  readonly isEnabled: boolean;
  requestSubscription(options: { serverPublicKey: string; }): Promise<PushSubscription>;
  unsubscribe(): Promise<void>;
}
```

### constructor

`SwPush`

@paramsw`NgswCommChannel`

@returns`SwPush`

### messages

`Observable<object>`

Emits the payloads of the received push notification messages.

### notificationClicks

`Observable<{ action: string; notification: NotificationOptions & { title: string; }; }>`

Emits the payloads of the received push notification messages as well as the action the user interacted with. If no action was used the `action` property contains an empty string `''`.

Note that the `notification` property does **not** contain a [Notification](https://developer.mozilla.org/en-US/docs/Web/API/Notification) object but rather a [NotificationOptions](https://notifications.spec.whatwg.org/#dictdef-notificationoptions) object that also includes the `title` of the [Notification](https://developer.mozilla.org/en-US/docs/Web/API/Notification) object.

### notificationCloses

`Observable<{ action: string; notification: NotificationOptions & { title: string; }; }>`

Emits the payloads of notifications that were closed, along with the action (if any) associated with the close event. If no action was used, the `action` property contains an empty string `''`.

Note that the `notification` property does **not** contain a [Notification](https://developer.mozilla.org/en-US/docs/Web/API/Notification) object but rather a [NotificationOptions](https://notifications.spec.whatwg.org/#dictdef-notificationoptions) object that also includes the `title` of the [Notification](https://developer.mozilla.org/en-US/docs/Web/API/Notification) object.

### pushSubscriptionChanges

`Observable<{ oldSubscription: PushSubscription | null; newSubscription: PushSubscription | null; }>`

Emits updates to the push subscription, including both the previous (`oldSubscription`) and current (`newSubscription`) values. Either subscription may be `null`, depending on the context:

- `oldSubscription` is `null` if no previous subscription existed.
- `newSubscription` is `null` if the subscription was invalidated and not replaced.

This stream allows clients to react to automatic changes in push subscriptions, such as those triggered by browser expiration or key rotation.

### subscription

`Observable<PushSubscription | null>`

Emits the currently active [PushSubscription](https://developer.mozilla.org/en-US/docs/Web/API/PushSubscription) associated to the Service Worker registration or `null` if there is no subscription.

### isEnabled

`boolean`

True if the Service Worker is enabled (supported by the browser and enabled via [`ServiceWorkerModule`](serviceworkermodule)).

### requestSubscription

`Promise<PushSubscription>`

Subscribes to Web Push Notifications, after requesting and receiving user permission.

@paramoptions`{ serverPublicKey: string; }`

An object containing the `serverPublicKey` string.

@returns`Promise<PushSubscription>`

### unsubscribe

`Promise<void>`

Unsubscribes from Service Worker push notifications.

@returns`Promise<void>`

## Usage Notes

You can inject a [`SwPush`](swpush) instance into any component or service as a dependency.

To subscribe, call [`SwPush.requestSubscription()`](swpush#requestSubscription), which asks the user for permission. The call returns a `Promise` with a new [`PushSubscription`](https://developer.mozilla.org/en-US/docs/Web/API/PushSubscription) instance.

A request is rejected if the user denies permission, or if the browser blocks or does not support the Push API or ServiceWorkers. Check [`SwPush.isEnabled`](swpush#isEnabled) to confirm status.

Invoke Push Notifications by pushing a message with the following payload.

```
{
  "notification": {
    "actions": NotificationAction[],
    "badge": USVString,
    "body": DOMString,
    "data": any,
    "dir": "auto"|"ltr"|"rtl",
    "icon": USVString,
    "image": USVString,
    "lang": DOMString,
    "renotify": boolean,
    "requireInteraction": boolean,
    "silent": boolean,
    "tag": DOMString,
    "timestamp": DOMTimeStamp,
    "title": DOMString,
    "vibrate": number[]
  }
}
```

Only `title` is required. See `Notification` [instance properties](https://developer.mozilla.org/en-US/docs/Web/API/Notification#Instance_properties).

While the subscription is active, Service Worker listens for [PushEvent](https://developer.mozilla.org/en-US/docs/Web/API/PushEvent) occurrences and creates [Notification](https://developer.mozilla.org/en-US/docs/Web/API/Notification) instances in response.

Unsubscribe using [`SwPush.unsubscribe()`](swpush#unsubscribe).

An application can subscribe to [`SwPush.notificationClicks`](swpush#notificationClicks) observable to be notified when a user clicks on a notification. For example:

You can read more on handling notification clicks in the [Service worker notifications guide](https://angular.dev/ecosystem/service-workers/push-notifications).

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/service-worker/SwPush>
