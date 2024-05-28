#!/usr/bin/env bash
KUSTOMIZE_BASE=$1
TEMPDIR=$(mktemp -d tmp.k8s.XXXXX)
delete_temp_dir() {
    if [ -d "$TEMPDIR" ]; then
        rm -r "$TEMPDIR"
    fi
}
trap delete_temp_dir EXIT
(
    cd "$TEMPDIR"
    kustomize create --resources ../$KUSTOMIZE_BASE
    for ((i=2; i<=$#; i++))
    do
        kustomize edit set image "${!i}"
    done
    kustomize build
)