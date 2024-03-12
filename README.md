# FastAPI_params

## Starting server

```bash
$ pdm run python src/main.py
```

## Making requests

```bash
$ http GET :8000/params/test_1 number==3 period:='{"start": "2023-01-01", "end": "2023-01-02"}'
{
    "test_1": {
        "end": "2023-01-02T00:00:00",
        "start": "2023-01-01T00:00:00"
    }
}
```

Sleep for 3 seconds and print on server side:

```txt
GET on /params endpoint with Path parameter name=test_1, Query parameter sleep=number=3 micro=False, and Body parameter period=2023-01-01 00:00:00 - 2023-01-02 00:00:00
```

### Optional micro Query parameter

```bash
$ http GET :8000/params/test_1 micro==True number==3 period:='{"start": "2023-01-01", "end": "2023-01-02"}'
```

Sleep for 0.3 seconds and print on server side:

```txt
GET on /params endpoint with Path parameter name=test_1, Query parameter sleep=number=3 micro=True, and Body parameter period=2023-01-01 00:00:00 - 2023-01-02 00:00:00

```
