# PRECONNECT_CHECK_BLOCKLIST

PRECONNECT\_CHECK\_BLOCKLIST



# PRECONNECT\_CHECK\_BLOCKLIST

Injection token to configure which origins should be excluded from the preconnect checks. It can either be a single string or an array of strings to represent a group of origins, for example:

## API

```
const PRECONNECT_CHECK_BLOCKLIST: InjectionToken<(string | string[])[]>;
```

## Description

Injection token to configure which origins should be excluded from the preconnect checks. It can either be a single string or an array of strings to represent a group of origins, for example:

```
 {provide: PRECONNECT_CHECK_BLOCKLIST, useValue: 'https://your-domain.com'}
```

or:

```
 {provide: PRECONNECT_CHECK_BLOCKLIST,
  useValue: ['https://your-domain-1.com', 'https://your-domain-2.com']}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/PRECONNECT_CHECK_BLOCKLIST>
