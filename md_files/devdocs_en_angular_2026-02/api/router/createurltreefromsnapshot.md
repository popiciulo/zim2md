# createUrlTreeFromSnapshot

createUrlTreeFromSnapshot



# createUrlTreeFromSnapshot

Creates a [`UrlTree`](urltree) relative to an [`ActivatedRouteSnapshot`](activatedroutesnapshot).

## API

```
function createUrlTreeFromSnapshot(
  relativeTo: ActivatedRouteSnapshot,
  commands: readonly any[],
  queryParams?: Params | null,
  fragment?: string | null,
  urlSerializer?: DefaultUrlSerializer,
): UrlTree;
```

### createUrlTreeFromSnapshot

`UrlTree`

Creates a [`UrlTree`](urltree) relative to an [`ActivatedRouteSnapshot`](activatedroutesnapshot).

@paramrelativeTo`ActivatedRouteSnapshot`

The [`ActivatedRouteSnapshot`](activatedroutesnapshot) to apply the commands to

@paramcommands`readonly any[]`

An array of URL fragments with which to construct the new URL tree. If the path is static, can be the literal URL string. For a dynamic path, pass an array of path segments, followed by the parameters for each segment. The fragments are applied to the one provided in the `relativeTo` parameter.

@paramqueryParams`Params | null`

The query parameters for the [`UrlTree`](urltree). `null` if the [`UrlTree`](urltree) does not have any query parameters.

@paramfragment`string | null`

The fragment for the [`UrlTree`](urltree). `null` if the [`UrlTree`](urltree) does not have a fragment.

@paramurlSerializer`DefaultUrlSerializer`

The [`UrlSerializer`](urlserializer) to use for handling query parameter normalization. You should provide your application's custom [`UrlSerializer`](urlserializer) if one is configured to parse and serialize query parameter values to and from objects other than strings/string arrays.

@returns`UrlTree`

Usage notes

```
// create /team/33/user/11
createUrlTreeFromSnapshot(snapshot, ['/team', 33, 'user', 11]);

// create /team/33;expand=true/user/11
createUrlTreeFromSnapshot(snapshot, ['/team', 33, {expand: true}, 'user', 11]);

// you can collapse static segments like this (this works only with the first passed-in value):
createUrlTreeFromSnapshot(snapshot, ['/team/33/user', userId]);

// If the first segment can contain slashes, and you do not want the router to split it,
// you can do the following:
createUrlTreeFromSnapshot(snapshot, [{segmentPath: '/one/two'}]);

// create /team/33/(user/11//right:chat)
createUrlTreeFromSnapshot(snapshot, ['/team', 33, {outlets: {primary: 'user/11', right:
'chat'}}], null, null);

// remove the right secondary node
createUrlTreeFromSnapshot(snapshot, ['/team', 33, {outlets: {primary: 'user/11', right: null}}]);

// For the examples below, assume the current URL is for the `/team/33/user/11` and the
`ActivatedRouteSnapshot` points to `user/11`:

// navigate to /team/33/user/11/details
createUrlTreeFromSnapshot(snapshot, ['details']);

// navigate to /team/33/user/22
createUrlTreeFromSnapshot(snapshot, ['../22']);

// navigate to /team/44/user/22
createUrlTreeFromSnapshot(snapshot, ['../../team/44/user/22']);
```

## Usage Notes

```
// create /team/33/user/11
createUrlTreeFromSnapshot(snapshot, ['/team', 33, 'user', 11]);

// create /team/33;expand=true/user/11
createUrlTreeFromSnapshot(snapshot, ['/team', 33, {expand: true}, 'user', 11]);

// you can collapse static segments like this (this works only with the first passed-in value):
createUrlTreeFromSnapshot(snapshot, ['/team/33/user', userId]);

// If the first segment can contain slashes, and you do not want the router to split it,
// you can do the following:
createUrlTreeFromSnapshot(snapshot, [{segmentPath: '/one/two'}]);

// create /team/33/(user/11//right:chat)
createUrlTreeFromSnapshot(snapshot, ['/team', 33, {outlets: {primary: 'user/11', right:
'chat'}}], null, null);

// remove the right secondary node
createUrlTreeFromSnapshot(snapshot, ['/team', 33, {outlets: {primary: 'user/11', right: null}}]);

// For the examples below, assume the current URL is for the `/team/33/user/11` and the
`ActivatedRouteSnapshot` points to `user/11`:

// navigate to /team/33/user/11/details
createUrlTreeFromSnapshot(snapshot, ['details']);

// navigate to /team/33/user/22
createUrlTreeFromSnapshot(snapshot, ['../22']);

// navigate to /team/44/user/22
createUrlTreeFromSnapshot(snapshot, ['../../team/44/user/22']);
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/createUrlTreeFromSnapshot>
