#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 /path/to/LIBERO" >&2
  exit 1
fi

ADDON_ROOT="$(cd "$(dirname "$0")" && pwd)"
LIBERO_ROOT="$(cd "$1" && pwd)"
DESTINATION="$LIBERO_ROOT/libero/libero/bddl_files/libero_risk"

if [ ! -d "$LIBERO_ROOT/libero/libero/bddl_files" ]; then
  echo "Not a LIBERO checkout: $LIBERO_ROOT" >&2
  exit 1
fi

mkdir -p "$DESTINATION"
rm -f \
  "$DESTINATION/KITCHEN_SCENE4_put_the_wine_bottle_in_front_of_the_top_drawer_and_open_it.bddl" \
  "$DESTINATION/KITCHEN_SCENE6_put_the_book_in_the_microwave_and_close_it.bddl" \
  "$DESTINATION/KITCHEN_SCENE6_put_the_moka_pot_in_the_microwave_and_close_it.bddl"
cp "$ADDON_ROOT"/scenes/*.bddl "$DESTINATION"/

SCENE_COUNT="$(find "$ADDON_ROOT/scenes" -maxdepth 1 -name '*.bddl' | wc -l | tr -d ' ')"
echo "Installed $SCENE_COUNT scene files in:"
echo "  $DESTINATION"
