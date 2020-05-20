# Developer Notes

Key things to be aware of when developing on this project.

## `ev3devsim` Hacking

The `ev3devsim` code runs under skulpt. To develop on the following packages:

- `ev3dev2/*` packages;
- `ev3dev2_glue.js`


the packages new to be built into the Skulpt distribution used by `nbev3devsim`. When updating those files, you need to:

- copy the updated files into a Skulpt repo `src/lib/` directory;
- in the Skulpt repo root directory, run `npm run dist`;
- grab the `skulpt-stdlib.js`, `skulpt.min.js` and `skulpt.min.js.map` files and copy them into `nbev3devsim/js/`.