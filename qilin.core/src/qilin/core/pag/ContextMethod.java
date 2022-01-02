/* Qilin - a Java Pointer Analysis Framework
 * Copyright (C) 2021-2030 Qilin developers
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as
 * published by the Free Software Foundation, either version 3.0 of the
 * License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Lesser Public License for more details.
 *
 * You should have received a copy of the GNU General Lesser Public
 * License along with this program.  If not, see
 * <https://www.gnu.org/licenses/lgpl-3.0.en.html>.
 */

package qilin.core.pag;

import soot.Context;
import soot.MethodOrMethodContext;
import soot.SootMethod;

public final class ContextMethod implements MethodOrMethodContext {
    private final SootMethod method;
    private final Context context;

    public SootMethod method() {
        return this.method;
    }

    public Context context() {
        return this.context;
    }

    public ContextMethod(SootMethod method, Context context) {
        this.method = method;
        this.context = context;
    }

    public int hashCode() {
        return this.method.hashCode() + this.context.hashCode();
    }

    public boolean equals(Object o) {
        if (!(o instanceof ContextMethod other)) {
            return false;
        } else {
            return this.method.equals(other.method) && this.context.equals(other.context);
        }
    }

    public String toString() {
        return "Method " + this.method + " in context " + this.context;
    }
}
