"""Windows single-instance protection for one runtime directory."""

import msvcrt
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path


class InstanceLockError(RuntimeError):
    """Exclusive ownership of the runtime directory was not obtained."""


@contextmanager
def single_instance(runtime_root: Path) -> Iterator[None]:
    """Hold an OS file lock until the context exits."""
    lock_path = runtime_root / "instance.lock"

    try:
        lock_file = lock_path.open("a+b")
    except OSError as exc:
        raise InstanceLockError("Cannot open the instance lock file.") from exc

    with lock_file:
        try:
            if lock_file.seek(0, 2) == 0:
                lock_file.write(b"\0")
                lock_file.flush()
            lock_file.seek(0)
            msvcrt.locking(lock_file.fileno(), msvcrt.LK_NBLCK, 1)
        except OSError as exc:
            raise InstanceLockError(
                "Cannot acquire the instance lock; another instance may be running."
            ) from exc

        try:
            yield
        finally:
            lock_file.seek(0)
            msvcrt.locking(lock_file.fileno(), msvcrt.LK_UNLCK, 1)
