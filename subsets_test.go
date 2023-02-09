package anagrams

import (
	"fmt"
	"testing"
)

func TestAllSubsets(t *testing.T) {
	type args struct {
		s string
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		{
			"VINYL",
			args{"VINYL"},
			"[VIN VIY VNY INY VINY VIL VNL INL VINL VYL IYL VIYL NYL VNYL INYL VINYL]",
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			have := fmt.Sprintf("%v", AllSubsets(tt.args.s))
			want := tt.want
			if have != want {
				t.Errorf("have=%s,want=%s", have, want)
			}
		})
	}
}
