package qilin.pta.toolkits.debloaterx;

import qilin.core.pag.AllocNode;
import qilin.core.pag.PAG;
import soot.SootMethod;

import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Validator {
    private final PAG pag;
    final DebloaterX pbf;

    public Validator(PAG pag, DebloaterX pbf) {
        this.pag = pag;
        this.pbf = pbf;
    }

    void validate() {
        Set<String> innerx = Stream.of(
                "<antlr.collections.impl.Vector: void <init>(int)>",
                "<antlr.collections.impl.Vector: java.lang.Object clone()>",
                "<antlr.collections.impl.Vector: void ensureCapacity(int)>",
                "<EDU.purdue.cs.bloat.tree.Expr: void <init>(EDU.purdue.cs.bloat.editor.Type)>",
                "<com.google.common.collect.HashMultimap: void <init>()>",
                "<com.sun.org.apache.xerces.internal.util.SymbolHash: void <init>()>",
                "<com.sun.org.apache.xerces.internal.util.SymbolHash: void <init>(int)>",
                "<com.sun.org.apache.xerces.internal.util.SymbolTable: void <init>(int)>",
                "<edu.umd.cs.findbugs.SortedBugCollection: void <init>(edu.umd.cs.findbugs.ProjectStats,java.util.Comparator)>",
                "<java.awt.Window: void init(java.awt.GraphicsConfiguration)>",
                "<java.lang.ThreadLocal$ThreadLocalMap: void <init>(java.lang.ThreadLocal$ThreadLocalMap)>",
                "<java.lang.ThreadLocal$ThreadLocalMap: void <init>(java.lang.ThreadLocal,java.lang.Object)>",
                "<java.lang.ThreadLocal$ThreadLocalMap: void resize()>",
                "<java.text.AttributedString: int ensureRunBreak(int,boolean)>",
                "<java.text.AttributedString: void createRunAttributeDataVectors()>",
                "<java.util.AbstractMap: java.util.Collection values()>",
                "<java.util.ArrayList: void <init>(int)>",
                "<java.util.Collections$SynchronizedMap: java.util.Collection values()>",
                "<java.util.Collections$SynchronizedMap: java.util.Set entrySet()>",
                "<java.util.Collections$SynchronizedMap: java.util.Set keySet()>",
                "<java.util.Collections$UnmodifiableMap: java.util.Set entrySet()>",
                "<java.util.concurrent.ConcurrentHashMap: java.util.Collection values()>",
                "<java.util.concurrent.ConcurrentHashMap: java.util.Set entrySet()>",
                "<java.util.concurrent.ConcurrentHashMap: java.util.Set keySet()>",
                "<java.util.HashMap: java.lang.Object clone()>",
                "<java.util.HashMap: java.util.Collection values()>",
                "<java.util.HashMap: java.util.Set entrySet0()>",
                "<java.util.HashMap: java.util.Set keySet()>",
                "<java.util.HashMap: void <init>()>",
                "<java.util.HashMap: void <init>(int,float)>",
                "<java.util.HashMap: void resize(int)>",
                "<java.util.HashSet: void <init>()>",
                "<java.util.HashSet: void <init>(int)>",
                "<java.util.HashSet: void <init>(int,float)>",
                "<java.util.HashSet: void <init>(int,float,boolean)>",
                "<java.util.HashSet: void <init>(java.util.Collection)>",
                "<java.util.Hashtable: java.lang.Object clone()>",
                "<java.util.Hashtable: void <init>(int,float)>",
                "<java.util.Hashtable: void rehash()>",
                "<java.util.IdentityHashMap: void init(int)>",
                "<java.util.IdentityHashMap: void resize(int)>",
                "<java.util.IdentityHashMap: java.util.Collection values()>",
                "<java.util.IdentityHashMap: java.util.Set entrySet()>",
                "<java.util.IdentityHashMap: java.util.Set keySet()>",
                "<java.util.TreeMap: java.util.Set entrySet()>",
                "<java.util.TreeMap: java.util.Collection values()>",
                "<java.util.ListResourceBundle: void loadLookup()>",
                "<java.util.TreeMap: java.util.NavigableMap subMap(java.lang.Object,boolean,java.lang.Object,boolean)>",
                "<java.util.TreeMap: java.util.NavigableSet navigableKeySet()>",
                "<java.util.TreeSet: java.lang.Object clone()>",
                "<java.util.TreeSet: void <init>()>",
                "<java.util.TreeSet: void <init>(java.util.Comparator)>",
                "<java.util.Vector: void <init>(int,int)>",
                "<java.util.WeakHashMap: java.util.Collection values()>",
                "<java.util.WeakHashMap: java.util.Set entrySet()>",
                "<java.util.WeakHashMap: java.util.Set keySet()>",
                "<java.util.WeakHashMap: void <init>()>",
                "<java.util.WeakHashMap: void <init>(int,float)>",
                "<java.util.WeakHashMap: void resize(int)>",
                "<javax.swing.text.AbstractDocument$BranchElement: void <init>(javax.swing.text.AbstractDocument,javax.swing.text.Element,javax.swing.text.AttributeSet)>",
                "<javax.swing.text.AbstractDocument$BranchElement: void replace(int,int,javax.swing.text.Element[])>",
                "<javax.swing.event.EventListenerList: void add(java.lang.Class,java.util.EventListener)>",
                "<javax.swing.event.EventListenerList: void remove(java.lang.Class,java.util.EventListener)>",
                "<org.apache.xml.utils.ObjectStack: java.lang.Object push(java.lang.Object)>",
                "<org.apache.xml.utils.ObjectVector: void <init>(int)>",
                "<org.eclipse.core.internal.registry.KeyedHashSet: void <init>(int,boolean)>",
                "<org.eclipse.core.internal.registry.KeyedHashSet: void expand()>",
                "<org.eclipse.core.internal.resources.MarkerSet: void <init>(int)>",
                "<org.eclipse.core.internal.resources.MarkerSet: void expand()>",
                "<org.eclipse.core.internal.runtime.ListenerList: void add(java.lang.Object)>",
                "<org.eclipse.core.internal.runtime.ListenerList: void remove(java.lang.Object)>",
                "<org.eclipse.core.internal.utils.Queue: void <init>(int,boolean)>",
                "<org.eclipse.core.internal.utils.Queue: void grow()>",
                "<org.eclipse.core.runtime.MultiStatus: void add(org.eclipse.core.runtime.IStatus)>",
                "<org.eclipse.debug.internal.core.ListenerList: void <init>(int)>",
                "<org.eclipse.debug.internal.core.ListenerList: void add(java.lang.Object)>",
                "<org.eclipse.debug.internal.core.ListenerList: void remove(java.lang.Object)>",
                "<org.eclipse.jdt.internal.compiler.parser.Parser: org.eclipse.jdt.internal.compiler.ast.CompilationUnitDeclaration parse(org.eclipse.jdt.internal.compiler.env.ICompilationUnit,org.eclipse.jdt.internal.compiler.CompilationResult,int,int)>",
                "<org.eclipse.jdt.internal.compiler.util.ObjectVector: void <init>()>",
                "<org.eclipse.jdt.internal.compiler.util.ObjectVector: void add(java.lang.Object)>",
                "<org.eclipse.jdt.internal.compiler.util.ObjectVector: void addAll(org.eclipse.jdt.internal.compiler.util.ObjectVector)>",
                "<org.eclipse.osgi.framework.internal.core.AbstractBundle: void initializeManifestLocalization()>",
                "<org.eclipse.osgi.framework.internal.core.KeyedHashSet: void <init>(int,boolean)>",
                "<org.eclipse.osgi.framework.internal.core.KeyedHashSet: void expand()>",
                "<org.eclipse.osgi.framework.util.Headers: void <init>(int)>",
                "<org.eclipse.osgi.framework.util.Headers: void add(java.lang.Object,java.lang.Object)>",
                "<org.jfree.util.AbstractObjectList: void <init>(int,int)>",
                "<org.jfree.util.AbstractObjectList: void set(int,java.lang.Object)>",
                "<sun.awt.util.IdentityArrayList: void <init>(int)>",
                "<sun.java2d.loops.RenderCache: void <init>(int)>",
                "<sun.java2d.loops.RenderCache: void put(sun.java2d.loops.SurfaceType,sun.java2d.loops.CompositeType,sun.java2d.loops.SurfaceType,java.lang.Object)>",
                "<java.util.Hashtable: java.util.Collection values()>",
                "<java.util.Hashtable: java.util.Set entrySet()>",
                "<java.util.Hashtable: java.util.Set keySet()>",
                "<javax.swing.JComponent: void <init>()>",
                "<net.sourceforge.pmd.ast.SimpleNode: void jjtAddChild(net.sourceforge.pmd.ast.Node,int)>",
                "<org.apache.lucene.index.MultiTermDocs: void <init>(org.apache.lucene.index.IndexReader[],int[])>",
                "<org.apache.lucene.util.PriorityQueue: void initialize(int)>",
                "<org.apache.xerces.util.SymbolHash: void <init>()>",
                "<org.apache.xerces.util.SymbolHash: void <init>(int)>",
                "<javax.swing.JComponent: javax.swing.ActionMap getActionMap(boolean)>",
                "<javax.swing.JComponent: javax.swing.ArrayTable getClientProperties()>",
                "<java.net.InetSocketAddress: void <init>(java.net.InetAddress,int)>",
                "<com.sun.org.apache.xerces.internal.util.SymbolHash: void put(java.lang.Object,java.lang.Object)>",
                "<java.lang.ThreadLocal$ThreadLocalMap: void set(java.lang.ThreadLocal,java.lang.Object)>",
                "<java.lang.ThreadLocal$ThreadLocalMap: void replaceStaleEntry(java.lang.ThreadLocal,java.lang.Object,int)>",
                "<java.util.Collections$UnmodifiableMap$UnmodifiableEntrySet: java.lang.Object[] toArray()>",
                "<java.util.concurrent.ConcurrentHashMap$Segment: java.lang.Object put(java.lang.Object,int,java.lang.Object,boolean)>",
                "<java.util.concurrent.ConcurrentHashMap$Segment: java.lang.Object remove(java.lang.Object,int,java.lang.Object)>",
                "<java.util.concurrent.ConcurrentHashMap$Segment: void rehash()>",
                "<java.util.HashMap: void addEntry(int,java.lang.Object,java.lang.Object,int)>",
                "<java.util.HashMap: void createEntry(int,java.lang.Object,java.lang.Object,int)>",
                "<java.util.Hashtable: java.lang.Object put(java.lang.Object,java.lang.Object)>",
                "<java.util.LinkedHashMap: void createEntry(int,java.lang.Object,java.lang.Object,int)>",
                "<java.util.WeakHashMap: java.lang.Object put(java.lang.Object,java.lang.Object)>",
                "<org.apache.xerces.util.SymbolHash: void put(java.lang.Object,java.lang.Object)>",
                "<java.util.concurrent.ConcurrentLinkedQueue: boolean offer(java.lang.Object)>",
                "<java.util.concurrent.ConcurrentLinkedQueue: void <init>()>",
                "<java.util.concurrent.LinkedBlockingQueue: void <init>(int)>",
                "<java.util.concurrent.LinkedBlockingQueue: void enqueue(java.lang.Object)>",
                "<java.util.LinkedHashMap: void init()>",
                "<java.util.LinkedList: boolean addAll(int,java.util.Collection)>",
                "<java.util.LinkedList: java.lang.Object clone()>",
                "<java.util.LinkedList: java.util.LinkedList$Entry addBefore(java.lang.Object,java.util.LinkedList$Entry)>",
                "<java.util.LinkedList: void <init>()>",
                "<java.util.TreeMap: java.lang.Object put(java.lang.Object,java.lang.Object)>"
        ).collect(Collectors.toSet());
        for (AllocNode heap : pag.getAllocNodes()) {
            SootMethod method = heap.getMethod();
            if (method == null || method.isStaticInitializer()) {
                continue;
            }
            if (innerx.contains(method.getSignature()) && !pbf.innerContainer.contains(heap)) {
                System.out.println("WHY not a inner container?" + heap);
//                if (heap.getMethod().getSignature().equals("<java.net.InetSocketAddress: void <init>(java.net.InetAddress,int)>")
//                        || heap.getMethod().getSignature().equals("<javax.swing.JComponent: javax.swing.ActionMap getActionMap(boolean)>")
//                ) {
//                    ctxDepHeaps.add(heap);
//                }
            }
        }

        // returned containers
        Set<String> returnedContainers = Stream.of(
                "<java.util.Arrays: java.lang.Object[] copyOf(java.lang.Object[],int,java.lang.Class)>",
                "<com.google.common.collect.Lists: java.util.ArrayList newArrayList()>",
                "<com.google.common.collect.Lists: java.util.LinkedList newLinkedList()>",
                "<com.google.common.collect.ImmutableMap: com.google.common.collect.ImmutableMap$Builder builder()>",
                "<com.google.common.collect.HashMultimap: com.google.common.collect.HashMultimap create()>",
                "<com.google.common.collect.ImmutableEnumMap: com.google.common.collect.ImmutableMap asImmutable(java.util.EnumMap)>",
                "<com.google.common.collect.ImmutableList: com.google.common.collect.ImmutableList construct(java.lang.Object[])>",
                "<com.google.common.collect.ImmutableMap$Builder: com.google.common.collect.ImmutableMap fromEntryList(java.util.List)>",
                "<com.google.common.collect.ImmutableMap: com.google.common.collect.ImmutableMap copyOf(java.util.Map)>",
                "<com.google.common.collect.ImmutableSortedSet: com.google.common.collect.ImmutableSortedSet construct(java.util.Comparator,int,java.lang.Object[])>",
                "<com.google.common.collect.Maps: java.util.HashMap newHashMap()>",
                "<com.google.common.collect.Maps: java.util.HashMap newHashMap(java.util.Map)>",
                "<com.google.common.collect.Maps: java.util.TreeMap newTreeMap()>",
                "<com.google.common.collect.RegularImmutableMap$EntrySet: com.google.common.collect.ImmutableList createAsList()>",
                "<com.google.common.collect.RegularImmutableMap: com.google.common.collect.ImmutableSet createEntrySet()>",
                "<com.google.common.collect.RegularImmutableMap: com.google.common.collect.RegularImmutableMap$LinkedEntry[] createEntryArray(int)>",
                "<com.google.common.collect.Sets: java.util.HashSet newHashSet()>",
                "<com.google.common.collect.Sets: java.util.HashSet newHashSet(java.lang.Iterable)>",
                "<com.google.common.collect.Sets: java.util.HashSet newHashSetWithExpectedSize(int)>",
                "<com.google.common.collect.Sets: java.util.LinkedHashSet newLinkedHashSet()>",
                "<com.google.common.collect.Sets: java.util.LinkedHashSet newLinkedHashSet(java.lang.Iterable)>",
                "<com.google.common.collect.Sets: java.util.TreeSet newTreeSet()>",
                "<java.util.Arrays: java.util.List asList(java.lang.Object[])>",
                "<java.util.concurrent.ConcurrentHashMap$HashEntry: java.util.concurrent.ConcurrentHashMap$HashEntry[] newArray(int)>",
                "<java.util.concurrent.ConcurrentHashMap$Segment: java.util.concurrent.ConcurrentHashMap$Segment[] newArray(int)>",
                "<java.util.WeakHashMap$EntrySet: java.util.List deepCopy()>",
                "<javax.swing.JRootPane: java.awt.Container createContentPane()>",
                "<javax.swing.JRootPane: javax.swing.JLayeredPane createLayeredPane()>",
                "<sun.awt.image.BufImgSurfaceData: sun.java2d.SurfaceData createData(java.awt.image.BufferedImage)>",
                "<sun.awt.image.BufImgSurfaceData: sun.java2d.SurfaceData createDataBC(java.awt.image.BufferedImage,sun.java2d.loops.SurfaceType,int)>",
                "<sun.awt.image.BufImgSurfaceData: sun.java2d.SurfaceData createDataBP(java.awt.image.BufferedImage,sun.java2d.loops.SurfaceType)>",
                "<sun.awt.image.BufImgSurfaceData: sun.java2d.SurfaceData createDataIC(java.awt.image.BufferedImage,sun.java2d.loops.SurfaceType)>",
                "<sun.awt.image.BufImgSurfaceData: sun.java2d.SurfaceData createDataSC(java.awt.image.BufferedImage,sun.java2d.loops.SurfaceType,java.awt.image.IndexColorModel)>",
                "<sun.java2d.pipe.SpanClipRenderer: java.lang.Object startSequence(sun.java2d.SunGraphics2D,java.awt.Shape,java.awt.Rectangle,int[])>",
                "<sun.security.jca.GetInstance: sun.security.jca.GetInstance$Instance getInstance(java.security.Provider$Service,java.lang.Class)>",
                "<com.google.common.collect.ImmutableBiMap: com.google.common.collect.ImmutableBiMap of(java.lang.Object,java.lang.Object)>",
                "<com.google.common.collect.ImmutableList: com.google.common.collect.ImmutableList asImmutableList(java.lang.Object[])>",
                "<com.google.common.collect.ImmutableSet: com.google.common.collect.ImmutableSet of(java.lang.Object)>",
                "<com.google.common.collect.ImmutableSortedSet: com.google.common.collect.ImmutableSortedSet emptySet(java.util.Comparator)>",
                "<com.google.common.collect.Maps: java.util.Map$Entry immutableEntry(java.lang.Object,java.lang.Object)>",
                "<com.google.common.collect.RegularImmutableMap: com.google.common.collect.RegularImmutableMap$LinkedEntry newLinkedEntry(java.lang.Object,java.lang.Object,com.google.common.collect.RegularImmutableMap$LinkedEntry)>",
                "<EDU.purdue.cs.bloat.tree.LocalExpr: java.lang.Object clone()>",
                "<edu.umd.cs.findbugs.ba.SourceFinder$ZipSourceRepository: edu.umd.cs.findbugs.ba.SourceFileDataSource getDataSource(java.lang.String)>",
                "<java.beans.FeatureDescriptor: java.lang.ref.Reference createReference(java.lang.Object,boolean)>",
                "<org.eclipse.jdt.internal.core.Member: org.eclipse.jdt.core.IType getType(java.lang.String,int)>"
        ).collect(Collectors.toSet());
        for (AllocNode heap : pag.getAllocNodes()) {
            SootMethod method = heap.getMethod();
            if (method == null || method.isStaticInitializer()) {
                continue;
            }
            if (returnedContainers.contains(method.getSignature()) && !pbf.containerFactory.contains(heap)) {
                System.out.println("WHY not a container in the factory?" + heap);
//                if (
//                        heap.toString().contains("new javax.swing.JPanel")
//                    || heap.toString().contains("new javax.swing.JLayeredPane")
//                ) {
//                    ctxDepHeaps.add(heap);
//                }
            }
        }

        // container wrapper
        Set<String> containerWrappers = Stream.of(
                "<java.util.AbstractCollection: java.lang.Object[] toArray()>",
                "<java.util.LinkedList: java.lang.Object[] toArray()>",
                "<java.util.AbstractCollection: java.lang.Object[] toArray()>",
                "<antlr.collections.impl.Vector: java.util.Enumeration elements()>",
                "<com.google.common.collect.AbstractMapBasedMultimap$WrappedCollection: java.util.Iterator iterator()>",
                "<com.google.common.collect.AbstractMapBasedMultimap: java.util.Collection wrapCollection(java.lang.Object,java.util.Collection)>",
                "<com.google.common.collect.AbstractMapBasedMultimap: java.util.List wrapList(java.lang.Object,java.util.List,com.google.common.collect.AbstractMapBasedMultimap$WrappedCollection)>",
                "<com.google.common.collect.ImmutableEnumMap$2: com.google.common.collect.UnmodifiableIterator iterator()>",
                "<com.google.common.collect.ImmutableEnumMap: com.google.common.collect.ImmutableSet createEntrySet()>",
                "<com.google.common.collect.ImmutableList: com.google.common.collect.UnmodifiableListIterator listIterator(int)>",
                "<com.google.common.collect.Iterators: com.google.common.collect.UnmodifiableListIterator forArray(java.lang.Object[],int,int,int)>",
                "<edu.umd.cs.findbugs.graph.AbstractGraph: java.util.Iterator outgoingEdgeIterator(edu.umd.cs.findbugs.graph.AbstractVertex)>",
                "<java.util.AbstractList: java.util.List subList(int,int)>",
                "<java.text.AttributedString: java.text.AttributedCharacterIterator getIterator(java.text.AttributedCharacterIterator$Attribute[],int,int)>",
                "<java.util.AbstractList: java.util.Iterator iterator()>",
                "<java.util.AbstractList: java.util.ListIterator listIterator(int)>",
                "<java.util.AbstractMap$2: java.util.Iterator iterator()>",
                "<java.util.Collections$SingletonSet: java.util.Iterator iterator()>",
                "<java.util.Collections$UnmodifiableCollection: java.util.Iterator iterator()>",
                "<java.util.Collections$UnmodifiableMap$UnmodifiableEntrySet: java.util.Iterator iterator()>",
                "<java.util.Collections: java.util.Collection synchronizedCollection(java.util.Collection,java.lang.Object)>",
                "<java.util.Collections: java.util.Collection unmodifiableCollection(java.util.Collection)>",
                "<java.util.Collections: java.util.Enumeration enumeration(java.util.Collection)>",
                "<java.util.Collections: java.util.List synchronizedList(java.util.List)>",
                "<java.util.Collections: java.util.List unmodifiableList(java.util.List)>",
                "<java.util.Collections: java.util.Map synchronizedMap(java.util.Map)>",
                "<java.util.Collections: java.util.Map unmodifiableMap(java.util.Map)>",
                "<java.util.Collections: java.util.Set synchronizedSet(java.util.Set)>",
                "<java.util.Collections: java.util.Set synchronizedSet(java.util.Set,java.lang.Object)>",
                "<java.util.Collections: java.util.Set unmodifiableSet(java.util.Set)>",
                "<java.util.concurrent.ConcurrentHashMap$EntrySet: java.util.Iterator iterator()>",
                "<java.util.concurrent.ConcurrentHashMap$KeySet: java.util.Iterator iterator()>",
                "<java.util.concurrent.ConcurrentHashMap$Values: java.util.Iterator iterator()>",
                "<java.util.HashMap: java.util.Iterator newEntryIterator()>",
                "<java.util.HashMap: java.util.Iterator newKeyIterator()>",
                "<java.util.HashMap: java.util.Iterator newValueIterator()>",
                "<java.util.Hashtable: java.util.Enumeration getEnumeration(int)>",
                "<java.util.Hashtable: java.util.Iterator getIterator(int)>",
                "<java.util.IdentityHashMap$EntrySet: java.util.Iterator iterator()>",
                "<java.util.IdentityHashMap$KeySet: java.util.Iterator iterator()>",
                "<java.util.IdentityHashMap$Values: java.util.Iterator iterator()>",
                "<java.util.LinkedHashMap: java.util.Iterator newEntryIterator()>",
                "<java.util.LinkedHashMap: java.util.Iterator newKeyIterator()>",
                "<java.util.LinkedHashMap: java.util.Iterator newValueIterator()>",
                "<java.util.LinkedList: java.util.ListIterator listIterator(int)>",
                "<java.util.ServiceLoader: java.util.Iterator iterator()>",
                "<java.util.SubList: java.util.ListIterator listIterator(int)>",
                "<java.util.TreeMap$AscendingSubMap$AscendingEntrySetView: java.util.Iterator iterator()>",
                "<java.util.TreeMap$EntrySet: java.util.Iterator iterator()>",
                "<java.util.TreeMap$Values: java.util.Iterator iterator()>",
                "<java.util.TreeMap: java.util.Iterator keyIterator()>",
                "<java.util.Vector: java.util.Enumeration elements()>",
                "<java.util.WeakHashMap$EntrySet: java.util.Iterator iterator()>",
                "<java.util.WeakHashMap$KeySet: java.util.Iterator iterator()>",
                "<java.util.WeakHashMap$Values: java.util.Iterator iterator()>",
                "<javax.swing.JComponent: javax.swing.JToolTip createToolTip()>",
                "<com.google.common.collect.Iterators: com.google.common.collect.UnmodifiableIterator singletonIterator(java.lang.Object)>",
                "<java.util.Collections$UnmodifiableMap$UnmodifiableEntrySet$1: java.util.Map$Entry next()>",
                "<java.util.Collections: java.util.List singletonList(java.lang.Object)>",
                "<java.util.Collections: java.util.Map singletonMap(java.lang.Object,java.lang.Object)>",
                "<java.util.Collections: java.util.Set singleton(java.lang.Object)>",
                "<java.util.concurrent.AbstractExecutorService: java.util.concurrent.RunnableFuture newTaskFor(java.lang.Runnable,java.lang.Object)>",
                "<java.util.concurrent.ConcurrentHashMap$EntryIterator: java.util.Map$Entry next()>",
                "<java.util.concurrent.Executors: java.util.concurrent.Callable callable(java.lang.Runnable,java.lang.Object)>",
                "<java.util.Hashtable$Entry: java.lang.Object clone()>",
                "<org.eclipse.debug.internal.core.ListenerList: java.lang.Object[] getListeners()>",
                "<org.eclipse.core.internal.resources.MarkerSet: org.eclipse.core.internal.resources.IMarkerSetElement[] elements()>",
                "<java.util.TreeMap: java.util.TreeMap$Entry buildFromSorted(int,int,int,int,java.util.Iterator,java.io.ObjectInputStream,java.lang.Object)>"
        ).collect(Collectors.toSet());
        for (AllocNode heap : pag.getAllocNodes()) {
            SootMethod method = heap.getMethod();
            if (method == null || method.isStaticInitializer()) {
                continue;
            }
            if (containerWrappers.contains(method.getSignature()) && !pbf.containerWrapper.contains(heap)) {
                System.out.println("WHY not a container  wrapper?" + heap);
//                ctxDepHeaps.add(heap);
            }
        }
        Set<String> special = Stream.of(
                "<EDU.purdue.cs.bloat.tree.Expr: void <init>(EDU.purdue.cs.bloat.editor.Type)>",
                "<EDU.purdue.cs.bloat.tree.PrintVisitor: void <init>(java.io.Writer)>",
                "<java.awt.geom.Rectangle2D: java.awt.geom.PathIterator getPathIterator(java.awt.geom.AffineTransform)>",
                "<java.beans.PropertyChangeSupport: void firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)>",
                "<java.io.DataInputStream: java.lang.String readLine()>",
                "<sun.nio.cs.StreamEncoder: sun.nio.cs.StreamEncoder forOutputStreamWriter(java.io.OutputStream,java.lang.Object,java.lang.String)>",
                "<sun.nio.cs.StreamDecoder: sun.nio.cs.StreamDecoder forInputStreamReader(java.io.InputStream,java.lang.Object,java.lang.String)>",
                "<java.util.zip.ZipInputStream: void <init>(java.io.InputStream)>"
        ).collect(Collectors.toSet());
        for (AllocNode heap : pag.getAllocNodes()) {
            SootMethod method = heap.getMethod();
            if (method == null || method.isStaticInitializer()) {
                continue;
            }
            if (special.contains(method.getSignature()) && !pbf.ctxDepHeaps.contains(heap)) {
                System.out.println("WHY not a special heap?" + heap);
//                ctxDepHeaps.add(heap);
            }
        }
    }
}
