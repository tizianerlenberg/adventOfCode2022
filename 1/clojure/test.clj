(require '[clojure.string :as str])

(def puzzle (slurp "puzzle.txt"))

(
    ->>(
        str/split puzzle #"\n\n"
    )
    (
        take 3
    )
    (
        for (
            print
        )
    )
)

(print "\n")
