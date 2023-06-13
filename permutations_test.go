package anagrams

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestPermutations(t *testing.T) {
	tests := []struct {
		name string
		s    string
		want []string
	}{
		{"length 3", "ABC", []string{"ABC", "ACB", "BAC", "BCA", "CAB", "CBA"}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			want := tt.want
			have := Permutations(tt.s)
			assert.Equal(t, want, have)
		})
	}
}
